import string
import re # Module for RegEx
import sys # Standard system library
import os # Standard module for system related operations

def checkmd5(userhash):
    valregrex = re.findall(r"([a-fA-F\d]{32})", userhash)
    if valregrex:
        return 1
    else:
        print("Invalid MD5 found!!")
        print("Exiting program error code: 2342")
        exit()
    print("Exiting program error code: 2343")
    exit()

def validatehashlen(userlen):
    valregrex = re.match(r"([0-9])", userlen)
    if valregrex:
        return 1
    else:
        print("Invalid Length Must be an Integer!!")
        print("Exiting program error code: 2352")
        exit()
    print("Exiting program error code: 2353")
    exit()
