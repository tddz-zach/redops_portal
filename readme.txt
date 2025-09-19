*********REDOPS PORTAL*********
1. RedOps Portal is a compact, Python + Bash offensive-security toolkit that automates reconnaissance, safe vulnerability discovery, local privilege-escalation checks, a lab-only reverse-shell demo, and automatic reporting — built for repeatable demos, internal assessments, and rapid red→blue handoffs.
2. A single-folder, dependency-light framework designed to show end-to-end offensive workflow for L1→L2 engineers. It runs in lab environments, saves machine-readable JSON outputs, and produces an instant HTML report so findings are presentation-ready and actionable for defenders.


Core capabilities (compact list):

Fast threaded TCP port scanner with polite HTTP probing.

HTTP enumeration (common files/dirs) and misconfiguration checks (.git, backups, .env).

Local privilege-escalation gatherer (SUID, world-writable files, sudo rules) for lab VMs.

Minimal, demonstrative encrypted reverse shell (lab only) to explain C2/persistence concepts.

Auto report generator that consolidates module outputs into outputs/report.html for immediate sharing.


NOTE : This project is designed strictly for authorized testing. Use only on systems you own or have explicit permission to test. Demo mode avoids network activity so you can present safely.