# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:46:11 2022

@author: sneha
"""

a=[]
d=[]
n=int(input("enter the size: "))
print("enter the elements: ")
for i in range(n):
    b=input("\n ")
    a.append(b)
for j in a:
    c=len(j)
    d.append(c)
print(d)