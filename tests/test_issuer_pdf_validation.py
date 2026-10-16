"""Offline synthetic regression tests; no ASX requests."""
import io
import unittest
from pypdf import PdfWriter
from scripts.issuer_pdf_validation import validate_pdf

def make_pdf(texts):
    # pypdf does not create text. Tests use a deterministic mocked reader below.
    return b"%PDF-synthetic"

class Page:
    def __init__(self, text): self.text = text
    def extract_text(self): return self.text

class Reader:
    def __init__(self, stream, strict=False):
        self.pages = PAGES

PAGES = []
class ClassificationTests(unittest.TestCase):
    def check(self, title, category, texts):
        global PAGES
        PAGES = [Page(t) for t in texts]
        from unittest.mock import patch
        with patch("scripts.issuer_pdf_validation.PdfReader", Reader):
            return validate_pdf(make_pdf(texts), title, category)

    def test_half_year_statements_after_page_twelve(self):
        pages = ["Half-year report for six months ended 31 December 2025 " * 3] * 20
        pages[16] += " Statement of financial position; statement of profit or loss"
        result = self.check("Half-year financial report", "HALF_YEAR", pages)
        self.assertEqual(result.status, "CANDIDATE_VALIDATED")
        self.assertEqual(result.marker_pages["position"], 17)

    def test_quarterly_activities_without_statements(self):
        result = self.check("Quarterly activities report", "QUARTERLY",
                            ["Quarterly activities report for quarter ended 30 June 2026 " * 4])
        self.assertEqual(result.status, "CANDIDATE_VALIDATED")
        self.assertEqual(result.subtype, "ACTIVITIES")

    def test_presentation_rejected(self):
        result = self.check("Half-year results presentation", "HALF_YEAR", ["text " * 30])
        self.assertEqual(result.status, "REJECTED")

    def test_ambiguous_period_requires_review(self):
        result = self.check("Annual report", "ANNUAL",
            ["Year ended 30 June 2025. Year ended 30 June 2026. "
             "Statement of financial position. Statement of profit or loss. " * 3])
        self.assertEqual(result.status, "REVIEW_REQUIRED")

    def test_invalid_pdf(self):
        result = validate_pdf(b"not pdf", "Annual report", "ANNUAL")
        self.assertEqual(result.status, "REJECTED")

    def test_no_quarterly_markers(self):
        result = self.check("Quarterly report", "QUARTERLY",
                            ["Quarter ended 30 June 2026; operational update " * 6])
        self.assertEqual(result.status, "REVIEW_REQUIRED")

if __name__ == "__main__":
    unittest.main()
