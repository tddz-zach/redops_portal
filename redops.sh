#!/usr/bin/env bash
# Quick demo runner (lab-only). Edit TARGET and HTTP_TARGET for your lab VM.

TARGET_IP="192.168.56.101"
HTTP_TARGET="http://192.168.56.101:80"

echo "[*] 1) Recon: quick scan (1-1024)"
python3 recon/recon.py ${TARGET_IP} 1 1024

echo "[*] 2) HTTP enum"
python3 enum/http_enum.py ${HTTP_TARGET}

echo "[*] 3) vuln checks (safe)"
python3 vuln/vuln_checks.py ${HTTP_TARGET}

echo "[*] 4) privesc (if running on target, copy privesc_local.py to target and run there)"
echo "[*] 5) generate report"
python3 report/report_gen.py
echo "[*] Report available at outputs/report.html"
