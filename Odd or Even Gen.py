# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:44:58 2022

@author: Admin
"""

print("\n\n\n\t\t\t\t\t ODD OR EVEN GENERATION")
print("\t\t\t\t\t ----------------------")
a=int(input("\n\n\t\t\t Enter starting of range : "))
b=int(input("\t\t\t Enter ending of range   : "))


print("\n\t\t\t EVEN NO. : ")
for i in range(a,b+1):
    if (i%2)==0:
        print("\t\t\t\t\t\t {0}".format(i))
        
        
print("\n\t\t\t ODD NO.  : ")  
for i in range(a,b+1):
    if (i%2)!=0:
       
        print("\t\t\t\t\t\t {0}".format(i))

    