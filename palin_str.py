# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:19:53 2022

@author: Admin
"""

print("\n\n\n\n\n\t\t\t\t\t\t PALINDROME OF STRING ")
print("\t\t\t\t\t\t ---------------- ")
while True:
    s=input("\n\n\t\t\t Enter a string : ")
    rev=""
    for i in s:
        rev=i+rev
    if s==rev:
        print("\n\n\t\t\t The given string (%s) is PALINDROME. "%rev)
    else:
        print("\n\n\t\t\t The given string (%s) is not a PALINDROME. "%s)
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break    
