#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(tgtHost,tgtPort):
   try:
      sock = socket(AF_INET, SOCK_STREAM)
      sock.connect((tgtHost,tgtPort))
      print (colored('[+]%d/tcp Open' %tgtPort, 'green'))
   except:
      print (colored('[-]%d/tcp Closed' %tgtPort, 'red'))
   finally:
      sock.close()

def portScan(tgtHost,tgtPorts):
   try:
      tgtIP = gethostbyname(tgtHost)
   except:
      print (colored('Cant Resolve the Target Host %s' %tgtHost, 'red'))
   try:
      tgtName = gethostbyaddr(tgtIP)
      print (colored('[+] Scan results for:' + tgtName[0], 'green'))
   except:
      print (colored('[+] Scan results for:' + tgtIP, 'green'))
   setdefaulttimeout(1)
   for tgtPort in tgtPorts :
      t = Thread(target=connScan, args=(tgtHost,int(t gtPort)))
      t.start()

def main():
   parser = optparse.OptionParser('Usage of program: '
                                 + '-H <target host>'
                                 + '-p <target port>')
   parser.add_option('-H', 
                     dest='tgtHost',
                     type='string',
                     help='Specify the host')
   parser.add_option('-p',
                     dest='tgtPorts',
                     type='string',
                     help='Specify the ports seperated by comma')
   (options,args) = parser.parse_args()
   tgtHost = options.tgtHost
   tgtPorts = str(options.tgtPorts).split(',')
   if(tgtHost == None) | (tgtPorts[0] == None):
      print (parser.usage)
      exit(0)
   portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
   main()