"""Conservative, offline ASX issuer PDF classification and validation.

No network access, no eligibility decisions. A positive result is a candidate
for analyst verification, not proof of regulatory reporting compliance.
"""
from __future__ import annotations

import hashlib
import io
import re
from dataclasses import asdict, dataclass
from datetime import date
from typing import Optional

from pypdf import PdfReader

ANNUAL = "ANNUAL"
HALF_YEAR = "HALF_YEAR"
QUARTERLY = "QUARTERLY"
TYPES = (ANNUAL, HALF_YEAR, QUARTERLY)
MAX_BYTES = 40 * 1024 * 1024
MAX_PAGES = 600
MAX_TEXT_CHARS = 2_000_000

EXCLUDED = re.compile(
    r"presentation|transcript|webcast|briefing|webinar|slides|"
    r"conference call|investor update|media release|notice of meeting",
    re.I,
)
TITLE_RULES = {
    ANNUAL: re.compile(r"annual (financial )?report|annual financial statements|"
                       r"appendix\s*4e\b|full.year financial statements|form\s*20.f\b", re.I),
    HALF_YEAR: re.compile(r"half.year(ly)? (financial )?(report|accounts|results|financial statements)|"
                          r"interim (financial )?(report|accounts|financial statements)|appendix\s*4d\b", re.I),
    QUARTERLY: re.compile(r"quarterly (activities|activity|cash.flow) report|"
                          r"appendix\s*[45][cb]\b|quarterly report", re.I),
}
STATEMENTS = {
    "position": re.compile(r"(statement of financial position|balance sheet)", re.I),
    "performance": re.compile(r"(statement of (profit or loss|comprehensive income)|income statement)", re.I),
    "cash_flows": re.compile(r"(statement of cash flows|cash flow statement)", re.I),
    "notes": re.compile(r"notes to (the )?(consolidated )?financial statements", re.I),
}
QUARTER_ACTIVITIES = re.compile(r"quarterly activities|quarterly activity|activities report", re.I)
QUARTER_CASH = re.compile(r"appendix\s*[45][cb]\b|quarterly cash.flow|"
                          r"cash flows from operating activities", re.I)
PERIOD = re.compile(
    r"(?:year|period|quarter|six months|half.year|three months|twelve months)"
    r"\s+(?:ended|ending|to)\s+(\d{1,2}\s+[A-Za-z]+\s+20\d{2}|"
    r"\d{1,2}[/-]\d{1,2}[/-]20\d{2})", re.I
)
DATE_FORMATS = ("%d %B %Y", "%d %b %Y", "%d/%m/%Y", "%d-%m-%Y")

@dataclass(frozen=True)
class Validation:
    status: str
    expected_type: str
    detected_type: str
    subtype: str
    period_end: Optional[str]
    pages_total: int
    pages_inspected: int
    markers: tuple[str, ...]
    marker_pages: dict[str, int]
    sha256: str
    reason: str

    def audit(self) -> dict:
        return asdict(self)


def _period(text: str) -> Optional[str]:
    dates = set()
    for match in PERIOD.finditer(text):
        raw = match.group(1)
        for fmt in DATE_FORMATS:
            try:
                dates.add(date.strptime(raw, fmt).isoformat())
                break
            except AttributeError:
                from datetime import datetime
                try:
                    dates.add(datetime.strptime(raw, fmt).date().isoformat())
                    break
                except ValueError:
                    continue
            except ValueError:
                continue
    # Multiple period ends must not be silently resolved to the latest one.
    return next(iter(dates)) if len(dates) == 1 else None


def validate_pdf(content: bytes, title: str, expected_type: str,
                 *, max_bytes: int = MAX_BYTES, max_pages: int = MAX_PAGES) -> Validation:
    """Fail closed on ambiguous identity, period or incomplete text inspection."""
    if expected_type not in TYPES:
        raise ValueError("Unsupported expected report type")
    digest = hashlib.sha256(content).hexdigest()
    def result(status, detected="UNKNOWN", subtype="", period=None, total=0,
               inspected=0, markers=(), marker_pages=None, reason=""):
        return Validation(status, expected_type, detected, subtype, period, total,
                          inspected, tuple(markers), marker_pages or {}, digest, reason)

    if EXCLUDED.search(title):
        return result("REJECTED", reason="Excluded non-report announcement title")
    title_types = [kind for kind, regex in TITLE_RULES.items() if regex.search(title)]
    if len(title_types) != 1 or title_types[0] != expected_type:
        return result("REVIEW_REQUIRED", reason="Title type missing, conflicting or mismatched")
    if len(content) > max_bytes:
        return result("REVIEW_REQUIRED", reason="PDF exceeds bounded byte limit")
    if not content.startswith(b"%PDF-"):
        return result("REJECTED", reason="Invalid PDF signature")
    try:
        reader = PdfReader(io.BytesIO(content), strict=False)
        total = len(reader.pages)
        if total == 0:
            return result("REJECTED", reason="Empty PDF")
        if total > max_pages:
            return result("REVIEW_REQUIRED", total=total, reason="Page limit exceeded")
        texts = []
        marker_pages = {}
        char_count = 0
        for index, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            char_count += len(text)
            if char_count > MAX_TEXT_CHARS:
                return result("REVIEW_REQUIRED", total=total, inspected=index + 1,
                              reason="Text extraction limit exceeded")
            texts.append(text)
            for name, pattern in STATEMENTS.items():
                if name not in marker_pages and pattern.search(text):
                    marker_pages[name] = index + 1
        full = "\n".join(texts)
    except Exception as exc:
        return result("REVIEW_REQUIRED", reason=f"PDF parse/extraction error: {type(exc).__name__}")
    if len(full.strip()) < 100:
        return result("REVIEW_REQUIRED", total=total, inspected=total,
                      reason="Insufficient extractable text; OCR/manual review needed")

    period = _period(full)
    subtype = ""
    detected = expected_type
    markers = tuple(sorted(marker_pages))
    if expected_type == QUARTERLY:
        activities = bool(QUARTER_ACTIVITIES.search(full))
        cash = bool(QUARTER_CASH.search(full))
        subtype = "ACTIVITIES_AND_CASH_FLOW" if activities and cash else (
            "ACTIVITIES" if activities else "CASH_FLOW" if cash else "UNKNOWN")
        if subtype == "UNKNOWN":
            return result("REVIEW_REQUIRED", detected, subtype, period, total, total,
                          markers, marker_pages, "Quarterly content identity unconfirmed")
    elif len(markers) < 2 or not ("position" in markers or "performance" in markers):
        return result("REVIEW_REQUIRED", detected, subtype, period, total, total,
                      markers, marker_pages, "Insufficient financial statement evidence")
    if period is None:
        return result("REVIEW_REQUIRED", detected, subtype, None, total, total,
                      markers, marker_pages, "Reporting period missing or ambiguous")
    return result("CANDIDATE_VALIDATED", detected, subtype, period, total, total,
                  markers, marker_pages, "Content evidence found; analyst period/type confirmation required")
