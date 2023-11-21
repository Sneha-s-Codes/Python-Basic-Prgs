# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:13:44 2022

@author: 19bit41
"""

print(" \n\n\t\t\t\t REMOVING DUPLICATES FROM THE LIST")
print("\n")

a=[]
n=int(input("\n\n\t\t\t Enter a no. of ele : "))
for x in range(0,n):
    e=int(input("\n\t\t\t Enter element "+str(x+1)+" : "))
    a.append(e)
b=set()
unique=[]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
        
print("\n\n\t\t\t Non-Duplicate items  : ", unique)

