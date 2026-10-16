#!/usr/bin/env python3
"""Best-effort issuer PDF collector. Unofficial ASX endpoint: verify permitted use before bulk runs."""
import argparse
import csv
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

DEFAULT_REGISTER = "research/01_universe_validation/registers/LEVEL_1_SCREENING_ELIGIBILITY_REGISTER.csv"
API = "https://asx.api.markitdigital.com/asx-research/1.0"
TYPES = ("annual", "half_year", "quarterly")
FIELDS = ("ASX_Code", "Report_Type", "Reporting_Period", "Publication_Date", "Source_URL", "File_Path", "Download_Status", "Document_Key", "SHA256", "Detail")
PATTERNS = {
    "annual": re.compile(r"annual report|appendix 4e|full.year financial (?:report|statements)", re.I),
    "half_year": re.compile(r"half.year (?:financial|report)|half yearly|appendix 4d|interim financial report", re.I),
    "quarterly": re.compile(r"appendix 4c|appendix 5b|quarterly (?:cash ?flow|activities and cash)", re.I),
}
EXCLUDE = re.compile(r"presentation|webcast|notice of meeting|corporate governance statement", re.I)


def load_codes(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if "ASX_Code" not in (reader.fieldnames or []):
            raise ValueError("Input CSV missing ASX_Code")
        codes = list(dict.fromkeys(row["ASX_Code"].strip().upper() for row in reader if row["ASX_Code"].strip()))
    if not codes:
        raise ValueError("No ASX codes found")
    return codes


def read_register(path):
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {(r["ASX_Code"], r["Report_Type"]): r for r in csv.DictReader(fh)}


def save_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def announcements(session, code, timeout):
    url = f"{API}/companies/{quote(code)}/announcements"
    response = session.get(url, params={"count": 200}, timeout=timeout)
    response.raise_for_status()
    body = response.json()
    data = body.get("data", body)
    if isinstance(data, dict):
        items = data.get("items", data.get("announcements"))
    else:
        items = data
    if not isinstance(items, list):
        raise ValueError("Unsupported announcement response schema")
    # Never infer completeness from a capped response.
    return items, len(items) >= 200


def select(items):
    result = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        title = str(item.get("headline") or item.get("title") or item.get("header") or "")
        if EXCLUDE.search(title):
            continue
        date = str(item.get("date") or item.get("releaseDate") or item.get("publishedAt") or "")
        key = item.get("documentKey")
        if not key or not date:
            continue
        for kind in TYPES:
            if PATTERNS[kind].search(title):
                candidate = (date, str(key), title)
                if kind not in result or candidate[0] > result[kind][0]:
                    result[kind] = candidate
    return result


def download(session, url, target, timeout):
    response = session.get(url, timeout=timeout, stream=True)
    response.raise_for_status()
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(".part")
    digest = hashlib.sha256()
    try:
        with temp.open("wb") as fh:
            for chunk in response.iter_content(65536):
                if chunk:
                    digest.update(chunk)
                    fh.write(chunk)
        with temp.open("rb") as fh:
            if fh.read(5) != b"%PDF-":
                raise ValueError("Response is not a PDF")
        temp.replace(target)
        return digest.hexdigest()
    finally:
        temp.unlink(missing_ok=True)


def run(args):
    codes = load_codes(args.input)
    if args.codes:
        requested = {c.strip().upper() for c in args.codes.split(",")}
        codes = [c for c in codes if c in requested]
    output = Path(args.output)
    register_path = output / "download_register.csv"
    existing = read_register(register_path)
    session = requests.Session()
    session.headers.update({"User-Agent": "ASXResearchIssuerCollector/0.1 (research; respectful access)", "Accept": "application/json,application/pdf"})
    for code in codes:
        try:
            items, capped = announcements(session, code, args.timeout)
            latest = select(items)
            for kind in TYPES:
                found = latest.get(kind)
                record = dict.fromkeys(FIELDS, "")
                record.update(ASX_Code=code, Report_Type=kind)
                if not found:
                    record.update(Download_Status="NOT_FOUND_IN_RESPONSE", Detail="Discovery results may be incomplete" if capped else "No matching announcement")
                else:
                    date, key, title = found
                    url = f"{API}/file/{quote(key, safe='')}"
                    target = output / "pdf" / code / kind / f"{re.sub('[^A-Za-z0-9_-]', '_', key)}.pdf"
                    record.update(Publication_Date=date, Source_URL=url, File_Path=str(target), Document_Key=key, Detail=title)
                    previous = existing.get((code, kind), {})
                    if target.is_file() and target.stat().st_size > 5 and previous.get("Document_Key") == key and previous.get("Download_Status") in ("DOWNLOADED", "ALREADY_PRESENT"):
                        record.update(Download_Status="ALREADY_PRESENT", SHA256=previous.get("SHA256", ""))
                    elif args.dry_run:
                        record["Download_Status"] = "DISCOVERED_NOT_DOWNLOADED"
                    else:
                        try:
                            record["SHA256"] = download(session, url, target, args.timeout)
                            record["Download_Status"] = "DOWNLOADED"
                        except (requests.RequestException, OSError, ValueError) as exc:
                            record.update(Download_Status="DOWNLOAD_ERROR", Detail=f"{title}: {type(exc).__name__}: {exc}")
                existing[(code, kind)] = record
        except (requests.RequestException, ValueError, KeyError) as exc:
            for kind in TYPES:
                existing[(code, kind)] = dict(ASX_Code=code, Report_Type=kind, Download_Status="DISCOVERY_ERROR", Detail=f"{type(exc).__name__}: {exc}")
        save_csv(register_path, [existing[k] for k in sorted(existing)], FIELDS)
        save_csv(output / "exceptions.csv", [r for r in existing.values() if r.get("Download_Status") not in ("DOWNLOADED", "ALREADY_PRESENT")], FIELDS)
        time.sleep(args.delay)
    print(json.dumps({"processed": len(codes), "register": str(register_path), "exceptions": str(output / "exceptions.csv")}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(DEFAULT_REGISTER))
    parser.add_argument("--output", default="research/issuer_reports")
    parser.add_argument("--codes", help="Comma-separated subset, e.g. ACW,ACE")
    parser.add_argument("--delay", type=float, default=2.0)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--dry-run", action="store_true")
    run(parser.parse_args())
