#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' #Standard loopback interface address(local host)
PORT = 9999	   #Port to listen on

with socket.socket(socket.AF_INET, socket_Stream) as  s:
	s.bind(HOST, PORT))
	s.sendall(b'Hello,Server')
	data = s.recv(1824)
	
print('Recieved',repr(data))