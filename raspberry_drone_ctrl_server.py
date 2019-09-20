#!/usr/bin/env python

from socket import *
import os

cmd = ['forward', 'backward', 'left', 'right', 'stop', 'disconnect']

HOST = ''
PORT = 3000
BUFSIZ = 1024  # Size of the buffer
ADDR = (HOST, PORT)

try:
    s = socket(AF_INET, SOCK_STREAM)   # Create a socket.
    s.bind(ADDR)    # Bind the IP address and port number of the server. 
    s.listen(5)
    print("Server is now running")
except:
  print("Could not create socket")

while True:
  print("Waiting for connection")
  tcpCliSock, address = s.accept()
  print("Connection created with %s", address)
  while True:
    data = ''
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
      break
    if data == cmd[0]:
      print("moving forward")
    elif data == cmd[1]:
      print("moving backward")
    elif data == cmd[2]:
      print("moving left")
    elif data == cmd[3]:
      print("moving right")
    elif data == cmd[4]:
      print("stopping car")
    elif data == cmd[5]:
      print("Disconnecting from", address)
      tcpCliSock.close()
    else:
      print("ERROR: no such command as -->", data)

print("Server has shut down")