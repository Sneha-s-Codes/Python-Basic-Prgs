# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:59:02 2022

@author: Admin
"""

print("\n\n\n\t\t\t STRING FUNCTIONS ")
print("\t\t\t ---------------- ")
while True:
    s=input("\n\t\t\t Enter the string : ")
    print("\n\t\t\t 1. Length of the string : %d" %len(s))
    print("\t\t\t 2. Largest ASCII Value in the string : %s" %max(s))
    print("\t\t\t 3. Smallest ASCII Value in the string : %s" %min(s))
    c=input("\t\t\t 4. Enter a Character : ")
    k=ord(c)
    print("\t\t\t ASCII Code : %d " %k)
    ch=input("\t\t\t 5. Enter a Character : ")
    a=(ch in s)
    print("\t\t\t Is the character in string?   : {0} ".format(a))
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
