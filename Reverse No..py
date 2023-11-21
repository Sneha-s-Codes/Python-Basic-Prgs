# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:19:30 2022

@author: Admin
"""

print("\n\n\n\t\t\t REVERSE NUMBER")
print("\t\t\t --------------")
while True:
    num=int(input("\n\n\t\t\t Enter a no. : "))
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
        
    print("\n\t\t\t REVERSE NO. : {0}".format(rev))
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
