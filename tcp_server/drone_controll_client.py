#!/usr/bin/env python

import socket
import os

test = ['disconnect', 'forward', 'backward', 'left', 'right', 'stop']
server_up = False;

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('192.168.43.143', 3000))
  server_up = True;
except:
  print("Server is not running")

if server_up:
    while True:
        cmd = input()
        if cmd != 'disconnect':
            print("Sending command cmd", cmd)
            s.sendall(bytes(cmd,'UTF-8'))
        else: 
            break
    s.close()



