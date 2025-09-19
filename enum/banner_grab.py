#!/usr/bin/env python3
"""
Banner grab and basic HTTP header fetch.
Usage: python3 banner_grab.py <target_ip> <port>
"""

import socket, sys
TARGET = sys.argv[1] if len(sys.argv) > 1 else None
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else None
TIMEOUT = 2.0

if not TARGET or not PORT:
    print("Usage: python3 banner_grab.py <target_ip> <port>")
    raise SystemExit(1)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((TARGET, PORT))
        if PORT in (80, 8080, 8000):
            s.send(b"HEAD / HTTP/1.0\r\nHost: example\r\n\r\n")
            data = s.recv(4096).decode(errors='ignore')
        else:
            # send a basic probe for common services
            s.send(b"\r\n")
            data = s.recv(4096).decode(errors='ignore')
        print(f"--- Banner for {TARGET}:{PORT} ---\n{data}\n-------------------------")
except Exception as e:
    print("Failed to grab banner:", e)
