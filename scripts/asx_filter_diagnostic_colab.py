#!/usr/bin/env python3
"""Conservative BHP ASX announcement filter diagnostic (no PDF downloads).

Experimental query keys are hypotheses, NOT verified ASX API parameters.
No access-control bypass, no credential collection, and no broad probing.
"""
import csv
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://asx.api.cmfyapp.com/asx-research/1.0"
XID = "199003248"  # BHP Group Limited; verify issuer independently
OUT = Path("/content/asx_filter_diagnostic")
OUT.mkdir(parents=True, exist_ok=True)
DELAY_SECONDS = 2.0
# Change this to test one or two specific hypotheses, e.g.
# [{"name": "date hypothesis", "params": {"fromDate": "2026-07-01", "toDate": "2026-10-17"}}]
# Keys in this example are NOT verified. Do not treat matching results as proof.
EXPERIMENTS = []
BASE_PARAMS = {
    "entityXids": XID,
    "page": 0,
    "itemsPerPage": 25,
    "summaryCountsDate": datetime.now(timezone.utc).date().isoformat(),
}
HEADERS = {"Accept": "application/json"}
SENSITIVE = {"authorization", "cookie", "x-api-key", "api-key", "token"}

def retrieve(session, params):
    time.sleep(DELAY_SECONDS)
    response = session.get(
        f"{BASE}/markets/announcements", params=params, timeout=45
    )
    if response.status_code in (401, 403, 429):
        raise RuntimeError(f"Access restriction HTTP {response.status_code}; stop testing")
    response.raise_for_status()
    data = response.json().get("data", {})
    if not isinstance(data.get("items"), list):
        raise ValueError("Unexpected response: data.items missing")
    items = data["items"]
    return {
        "http_status": response.status_code,
        "total": data.get("count"),
        "returned": len(items),
        "keys": [str(x.get("documentKey", "")) for x in items],
        "samples": [
            {"date": x.get("date"), "headline": x.get("headline"),
             "documentKey": x.get("documentKey"),
             "category_fields": {k: v for k, v in x.items()
                 if any(s in k.lower() for s in ("type", "category", "class"))}}
            for x in items[:10]
        ],
    }

def main():
    if os.environ.get("ASX_AUTOMATED_ACCESS_AUTHORISED") != "YES":
        raise PermissionError("Confirm access authorisation before setting ASX_AUTOMATED_ACCESS_AUTHORISED=YES")
    if len(EXPERIMENTS) > 3:
        raise ValueError("At most three controlled experiments per run")
    with requests.Session() as session:
        session.headers.update(HEADERS)
        baseline = retrieve(session, BASE_PARAMS)
        print("BASELINE", "total=", baseline["total"], "returned=", baseline["returned"])
        rows = [{"experiment": "baseline", "parameters": BASE_PARAMS,
                 "result": baseline, "same_as_baseline": None}]
        for experiment in EXPERIMENTS:
            params = dict(BASE_PARAMS)
            overrides = experiment["params"]
            if any(k.lower() in SENSITIVE for k in overrides):
                raise ValueError("Do not include credentials in diagnostic parameters")
            params.update(overrides)
            result = retrieve(session, params)
            same = (result["total"] == baseline["total"]
                    and result["keys"] == baseline["keys"])
            rows.append({"experiment": experiment["name"],
                         "parameters": params, "result": result,
                         "same_as_baseline": same})
            print(experiment["name"], "total=", result["total"],
                  "returned=", result["returned"], "same_as_baseline=", same)
    output = OUT / "bhp_filter_diagnostic.json"
    output.write_text(json.dumps({
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "endpoint": f"{BASE}/markets/announcements",
        "warning": "Response differences alone do not prove parameter semantics; identical responses may mean ignored filters.",
        "experiments": rows
    }, indent=2), encoding="utf-8")
    print("Saved:", output)
    print("No PDFs downloaded; no repository screening data changed.")

if __name__ == "__main__":
    main()
