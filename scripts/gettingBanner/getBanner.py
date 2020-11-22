#!/usr/bin/python3

import socket
from termcolor import colored

def retBanner(ipaddr, port):
   try:
      socket.setdefaulttimeout(2)
      s = socket.socket()
      s.connect((ipaddr, port))
      banner = s.recv(1024)
      return banner
   except:
      return

def main():
   ipaddr = input(" [*] Enter the ip you need to scan : ")
   portlist = [21, 22, 25, 80, 110, 443, 445]
   for port in portlist:
      banner = retBanner(ipaddr, port)
      if banner :
         print(colored('[+] ' + ipaddr + "::" + str(port) + " : " + str(banner).strip('/n'), 'green'))
      else :
         print(colored('[-] ' + ipaddr + "::" + str(port) + " : Port is not open!", 'red'))

if __name__ == '__main__':
   main()