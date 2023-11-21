# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:08:46 2022

@author: Admin
"""
print("\n\n\n\n\t\t\t SUM OF DIGITS")
print("\t\t\t ~~~~~~~~~~~~~")
while True:
    num=input("\n\n\t\t\t Enter a number: ")
    sum=0
    for n in num:
        sum=sum+int(n)
    print("\n\n\t\t\t SUM OF DIGITS: {0}".format(sum))
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
