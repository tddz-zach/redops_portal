#!/usr/bin/env python3
"""
Collect outputs/*.json and generate a simple HTML report in outputs/report.html
Usage: python3 report_gen.py
"""
import json, os, glob
outdir = "../outputs"
files = glob.glob(outdir + "/*.json")
report_items = []
for f in files:
    try:
        data = json.load(open(f))
        report_items.append((os.path.basename(f), data))
    except Exception:
        pass

html = "<html><head><meta charset='utf-8'><title>RedOps Report</title></head><body>"
html += "<h1>RedOps Portal - Auto Report</h1>"
for name, data in report_items:
    html += f"<h2>{name}</h2><pre>{json.dumps(data, indent=2)}</pre>"

html += "</body></html>"
open(outdir + "/report.html","w").write(html)
print("[+] Report generated at outputs/report.html")
