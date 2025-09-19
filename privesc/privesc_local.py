#!/usr/bin/env python3
"""
Local privesc info gatherer. Run this on the target Linux VM (lab).
Collects: kernel info, sudo -l, world-writable files, SUID binaries.
Usage: python3 privesc_local.py
"""

import os, subprocess, json

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode()
    except Exception as e:
        return str(e)

info = {}
info['uname'] = run("uname -a")
info['os_release'] = run("cat /etc/os-release")
info['sudoers'] = run("sudo -l 2>&1")  # will prompt if sudo needs password - run as permitted user
info['suid'] = run("find / -perm -4000 -type f -exec ls -ld {} \\; 2>/dev/null | head -n 200")
info['world_writable'] = run("find / -xdev -type f -perm -0002 -ls 2>/dev/null | head -n 200")
info['crontab'] = run("ls -la /etc/cron* 2>/dev/null || true")
# Save
os.makedirs("../outputs", exist_ok=True)
with open("../outputs/privesc_local.json", "w") as f:
    json.dump(info, f, indent=2)
print("[+] privesc info collected and saved to outputs/privesc_local.json")
