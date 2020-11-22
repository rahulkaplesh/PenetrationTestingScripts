#!/usr/bin/python3

import hashlib
from termcolor import colored

def main():
   hashValue = input(colored('[*] Enter a string to hash : ', 'yellow'))
   hashObj1 = hashlib.md5()
   hashObj1.update(hashValue.encode())
   print(colored('MD5    Hash value is : ' + hashObj1.hexdigest(), 'green'))
   hashObj2 = hashlib.sha1()
   hashObj2.update(hashValue.encode())
   print(colored('SHA1   Hash value is : ' + hashObj2.hexdigest(), 'green'))
   hashObj3 = hashlib.sha224()
   hashObj3.update(hashValue.encode())
   print(colored('SHA224 Hash value is : ' + hashObj3.hexdigest(), 'green'))
   hashObj4 = hashlib.sha256()
   hashObj4.update(hashValue.encode())
   print(colored('SHA256 Hash value is : ' + hashObj4.hexdigest(), 'green'))
   hashObj5 = hashlib.sha512()
   hashObj5.update(hashValue.encode())
   print(colored('SHA512 Hash value is : ' + hashObj5.hexdigest(), 'green'))

if __name__ == '__main__':
   main()