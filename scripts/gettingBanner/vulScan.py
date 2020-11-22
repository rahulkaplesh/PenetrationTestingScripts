#!/usr/bin/python3

import socket
import os
import sys
from termcolor import colored
from getBanner import retBanner

def checkVulns(banner, filename):
   f = open(filename, "r")
   for line in f.readlines():
      if line.strip("\n") in str(banner):
         print(colored('[+] Server is vulnerable: ' + str(banner).strip("\n"), 'red'))


def main():
   if len(sys.argv) == 2:
      filename = sys.argv[1]
      if not os.path.isfile(filename):
         print(colored("[-] File does not exists", 'red'))
      if not os.access(filename, os.R_OK):
         print(colored("[-] Access Denied", 'red'))
   else:
      print(colored("[H] Usage:" + str(sys.argv[0]) + " <vuln filename>", 'red'))
   portlist = [21, 22, 25, 80, 110, 443, 445]
   addrRange = "10.0.2."
   for i in range(4,5):
      ipaddr = addrRange + str(i)
      for port in portlist:
         banner = retBanner(ipaddr, port)
         if banner :
            print(colored('[+] ' + ipaddr + "::" + str(port) + " : " + str(banner).strip('/n'), 'green'))
            checkVulns(banner, filename)
         else :
            print(colored('[-] ' + ipaddr + "::" + str(port) + " : Port is not open!", 'red'))

if __name__ == "__main__":
   main()