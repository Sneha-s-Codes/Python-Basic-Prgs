# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:17:46 2022

@author: Admin
"""

print("\n\n\n\t\t\t\t CONVERSION FARHENHIET TO CENTIGRADE ")
print("\t\t\t\t ----------------------------------- ")
while True:
    f=float(input("\n\n\t\t\t Enter the farhenhiet : "))
    c=(f-32)*(5/9)
    print("\n\n\t\t\t Centigrade    : %5.2f"%c)
    
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
    print("\n\t-------------------------------------------------")
    