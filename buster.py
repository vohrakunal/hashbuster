import string
import re # Module for RegEx
import sys # Standard system library
import os # Standard module for system related operations
from itertools import permutations, product, combinations_with_replacement
from decorations import *
import time
import itertools
import hashlib

def commpassverify(userhash):
    items = 0
    fileopen = open("commonpass.txt","r")
    itemsoffile = fileopen.readlines()
    totaliter = len(itemsoffile)
    for text in itemsoffile:
        if items%2 == 0:
            sys.stdout.write("\r%s Processed: %s  Total: %s  /" %(green, items, totaliter) )
        else:
            sys.stdout.write("\r%s Processed: %s  Total: %s  \ " %(green, items, totaliter) )

        sys.stdout.flush()

        items = items + 1
        m = hashlib.md5()
        # time.sleep(0.0001)
        textval = text.strip()
        m.update(textval.encode('utf-8'))
        hashres = m.hexdigest()
        if userhash == hashres:
            print("%s Found!! HEXCODE: %s Value: %s " %(ok, userhash, textval))
            return 1
    sys.stdout.write("\n%s Processed: %s  Total: %s " %(complete, items, totaliter) )
    sys.stdout.flush()
    print("\n %s Sorry!! Could not find the value\n" %nosuccess)
    return 0

def burstfunc(userhash,hashlen,upper,special,timer):
    alphalower = list(string.ascii_lowercase[:])
    alphaupper = list(string.ascii_uppercase[:])
    allstrings = list(string.printable)
    alphaset = alphalower
    items = 0

    listfile = list()
    if upper == 'y':
        alphaset = alphaset + alphaupper
    if special == 'y':
        alphaset = allstrings

    valuefinal = list(itertools.product(sorted(list(alphaset)), repeat = int(hashlen)))
    lenofiter = len(valuefinal)
    for val in valuefinal:
        m = hashlib.md5()
        if items%2 == 0:
            sys.stdout.write("\r%s Processed: %s  Total: %s / " %(green, items, lenofiter) )
        else:
            sys.stdout.write("\r%s Processed: %s  Total: %s \ " %(green, items, lenofiter) )

        sys.stdout.flush()
        if timer == 'y':
            time.sleep(0.0001)
        items = items+1
        str = ("".join(val))
        m.update(str.encode('utf-8'))
        result = m.hexdigest()
        if userhash == result:
            print("\n\n\n%s Value Found!! \n %s HEXCODE: %s \n %s Value: %s" %(ok, que, userhash,que, str))
            time.sleep(1)
            return 1
    print("%s Sorry!! Could not find the value" %nosuccess)
    return 0
