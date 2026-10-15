#!/usr/bin/env python3
"""Functional smoke/regression tests for the four migrated research scripts."""
import csv
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

def run(script, *args):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                          cwd=ROOT, capture_output=True, text=True)

def csv_file(path, columns, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)

class ResearchScriptRegression(unittest.TestCase):
    def test_duplicate_audit_real_dataset(self):
        result = run("audit_operating_duplicates.py")
        self.assertIn("Records:", result.stdout)
        self.assertIn("unique tickers:", result.stdout)
        self.assertIn(result.returncode, (0, 1))
        self.assertNotIn("Traceback", result.stderr)

    def test_duplicate_audit_fixture(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "candidates.csv"
            csv_file(p, ["ASX_Code", "Company_Name"], [
                ["AAA", "Alpha Limited"], ["BBB", "Beta Limited"]])
            good = run("audit_operating_duplicates.py", p)
            self.assertEqual(good.returncode, 0, good.stderr)
            csv_file(p, ["ASX_Code", "Company_Name"], [
                ["AAA", "Alpha Limited"], ["AAA", "Alpha Limited"]])
            bad = run("audit_operating_duplicates.py", p)
            self.assertEqual(bad.returncode, 1, bad.stderr)
            self.assertIn("Duplicate tickers: 1", bad.stdout)

    def test_crossmatch_fixture(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            c = d / "c.csv"
            h = d / "page.html"
            csv_file(c, ["ASX_Code", "Company_Name"], [["NEW", "New Ltd"]])
            h.write_text("<table><tr><td>1 Jan</td><td>OLD</td><td>Old Ltd</td>"
                         "<td>NEW</td><td>New Ltd</td></tr></table>")
            result = run("crossmatch_asx_code_changes.py", c, h)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = list(csv.DictReader(io.StringIO(result.stdout)))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["change_type"], "CODE_CHANGE")
            self.assertEqual(rows[0]["matched_candidate"], "NEW")

    def test_directory_fixture(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            c, official, out = d/"c.csv", d/"official.csv", d/"result.csv"
            csv_file(c, ["ASX_Code", "Company_Name"], [
                ["AAA", "Alpha Limited"], ["BBB", "Beta Limited"],
                ["CCC", "Gamma Limited"]])
            csv_file(official, ["ASX_Code", "Company_Name"], [
                ["AAA", "Alpha Limited"], ["BBB", "Unrelated Holdings"]])
            result = run("verify_asx_directory.py", "--candidates", c,
                         "--directory", official, "--output", out)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = list(csv.DictReader(out.open()))
            self.assertEqual([row["Result"] for row in rows],
                             ["MATCHED", "NAME_REVIEW", "MISSING"])
            self.assertTrue(all(row["Listing_Status"] == "NOT_CHECKED" for row in rows))

    def test_primary_code_change_parser_fixture(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            matrix, page, output = d/"matrix.csv", d/"page.html", d/"out"
            csv_file(matrix, ["ASX_Code"], [["NEW"]])
            tabs = []
            for year in range(2018, 2027):
                data = json.dumps({"x": {"dc:title": str(year)}}).replace('"', "&quot;")
                tabs.append(
                    f'<div role="tabpanel" data-cmp-data-layer="{data}">'
                    '<table><tr><td>1 Jan</td><td>OLD</td><td>Old Ltd</td>'
                    '<td>NEW</td><td>New Ltd</td></tr></table></div>')
            page.write_text("<html><body>" + "".join(tabs) + "</body></html>")
            result = run("audit_primary_code_changes.py", "--html", page,
                         "--matrix", matrix, "--output-dir", output,
                         "--cutoff", "2026-10-13")
            self.assertEqual(result.returncode, 0, result.stderr)
            qa = json.loads((output/"asx_code_changes_qa.json").read_text())
            self.assertEqual(qa["source_rows"], 9)
            self.assertEqual(qa["matched_event_rows"], 9)
            self.assertEqual(qa["parse_errors"], [])
            self.assertEqual(len(list(csv.DictReader(
                (output/"asx_code_changes_population.csv").open()))), 9)

if __name__ == "__main__":
    unittest.main(verbosity=2)
