
# Designed by kv
# github.com/kunalvohra94
# ver 2.8.4

import string
import os # Standard module for system related operations
from itertools import combinations_with_replacement
from buster import burstfunc, commpassverify
from validate import checkmd5
from validate import validatehashlen
from decorations import *
import time


print("\n\n%s Hash Buster \tv2.8.4" %yellow)
print("%s Designed by kv" %white)
print("%s www.github.com/kunalvohra94\n" %white)
print("%s For any Suggestions please write to kunalvohra1994@gmail.com\n\n" %green)

print("%s This program might freeze your PC!!" %warn)


print("%s I am not responsible for Bricked Devices!!\n" %warn)

time.sleep(1)
userhash = input("%s Enter the hash value in md5: " %quest)

if not userhash:
    print("%s Please Enter a hash value" %warn)
    print("%s Exiting program error code: 2341" %error)
    exit()
else:
    chkrtnhash = checkmd5(userhash)


if chkrtnhash != 1:
    print("%s Exiting program error code: 2344" %error)
    exit()

userhash = userhash.lower()
commpass = input("%s Do you want to check for Common Passwords? (Y/n)" %quest)
commpass = commpass.lower()
if (commpass != 'y') and (commpass != 'n'):
    print("%s Invalid Option" %warn)
    print("%s Exiting program error code: 2391" %error)
    exit()
elif (commpass == 'y'):
    rtncommpass = commpassverify(userhash)
    if rtncommpass == 1:
        print("%s MD5 decrypted Sucessfully :) Thanks" %finish)
        exit()

brutequest = input("%s Do you want to Try Brute Force Method? (Y/n)" %quest)
if (brutequest != 'y') and (brutequest != 'n'):
    print("%s Invalid Option" %warn)
    print("%s Exiting program error code: 2301" %error)
    exit()
if (brutequest == 'n'):
    print("%s Exiting Program.. Thanks" %finish)
    exit()

print("\n\n----------------Initilaizing Brute Force------------------------\n")

hashlen = input("%s Max possible length of string in plain text (Press Enter for default: 5) [Recommended Range 1-15] " %quest)
if not hashlen:
    print("%s Setting default Value: 5" %exe)
    hashlen = '5'
else:
    chkrtlen = validatehashlen(hashlen)

    if chkrtlen != 1:
        print("%s Exiting program error code: 2354" %error)
        exit()


upper = input("%s Do you want to check for Upper Case [Y/n] " %quest)
upper = upper.lower()
if (upper != 'y') and (upper != 'n'):
    print("%s Invalid Option" %warn)
    print("%s Exiting program error code: 2361" %error)
    exit()

print("%s Use of Special Charaters might take longer time !!" %warn)
special = input("%s Do you want to check for Special Characters(like [0-9],@,#,$ etc)[Y/n] " %quest)
special = special.lower()
if (special != 'y') and (special != 'n'):
    print("%s Invalid Option" %warn)
    print("%s Exiting program error code: 2371" %error)
    exit()


# ADD TIMER TO SLOW DOWN
timer = input("%s Add delay timer of 0.0001s (Useful for low end PC) [Y/n] " %quest)

timer = timer.lower()
if (timer != 'y') and (timer != 'n'):
    print("%s Invalid Option" %warn)
    print("%s Exiting program error code: 2381" %error)
    exit()



print("\n\n-----     Finalizing Inputs     -----\n")

print("%s MD5 Hash: %s" % (que, userhash))
print("%s Length: %s" % (que, hashlen))
print("%s Upper Case: %s" % (que, upper))
print("%s Special Characters: %s" % (que, special))
print("%s Using Timer: %s" % (que, timer))


burstrtn = burstfunc(userhash,hashlen,upper,special,timer)

if burstrtn == 1:
    print("%s \n MD5 decrypted Sucessfully :) Thanks \n " %finish)
    exit()
elif burstrtn == 0:
    print("%s Sorry Please try with different Length and Combination" %finish)
    exit()
else:
    print("%s Invalid Result Found" %warn)
    print("%s Exiting program error code: 2401" %error)
    exit()
