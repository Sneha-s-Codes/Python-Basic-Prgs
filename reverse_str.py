# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:08:19 2022

@author: Admin
"""

print("\n\n\n\n\n\t\t\t\t\t REVERSE A STRING ")
print("\t\t\t\t\t ---------------- ")
while True:
    s=input("\n\n\t\t\t Enter a string : ")
    rev=""
    for i in s:
        rev=i+rev 
    print("\n\n\t\t\t REVERSED STRING : %s"%rev)
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
