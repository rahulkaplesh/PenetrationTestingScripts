#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ## Connects on ipv4 on tcp protocol
socket.setdefaulttimeout(1)

host = input("[*] Enter the host to scan: ")

def portscanner(port):
   if sock.connect_ex((host,port)):
      print (colored("Port %d is closed" % (port), 'red'))
   else:
      print (colored("Port %d is open" % (port), 'green'))

for port in range(440,450):
   portscanner(port)