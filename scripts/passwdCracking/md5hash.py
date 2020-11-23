#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored

def main():
   md5hash = input(colored('[*] Enter the MD5 hash to be cracked : ', 'yellow'))
   passList = str(urlopen('https://raw.githubusercontent.com/rahulkaplesh/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
   for password in passList.split('\n'):
      hashGuess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
      if hashGuess == md5hash:
         print(colored('[+] Password is : ' + password, 'green'))
         return
      else:
         print(colored('[-] Password guess : ' + password + ' does not match', 'red'))

if __name__ == '__main__':
   main()