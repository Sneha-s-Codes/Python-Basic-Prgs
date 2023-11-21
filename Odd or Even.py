# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:37:12 2022

@author: Admin
"""

print("\n\n\n\t\t\t\t\t ODD OR EVEN CHECKING")
print("\t\t\t\t\t --------------------")
while True:
    n=int(input("\n\n\t\t\t Enter a no. to be checked : "))
    if (n%2)==0:
        print("\n\n\t\t\t The given no. ({0}) is EVEN.".format(n))
    else:
        print("\n\n\t\t\t The given no. ({0}) is ODD.".format(n))
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
