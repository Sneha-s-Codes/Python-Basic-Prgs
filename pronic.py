# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:32:43 2022

@author: Admin
"""

print("\n\n\n\t\t\t PRONIC NUMBER GENERATION")
print("\t\t\t ------------------------")
while True:
    a=int(input("\n\n\n\t\t\t Enter the starting value : "))
    b=int(input("\t\t\t Enter the ending value   : "))
    s=""
    print("\n\n\t\t\t PRONIC NUMBERS :")
    for i in range(a,b+1):
        s=(i*(i+1))
        print("\t\t\t\t\t\t\t\t {0}".format(s))
    if input("\n\n\t\t\t Do you want to continue?  : ") !='y':
        break
    print("\n\t-------------------------------------------------")

