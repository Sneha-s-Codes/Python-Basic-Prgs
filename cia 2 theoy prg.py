# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 05:34:41 2022

@author: sneha
"""

li=[]
print("\n\n\n\t\t\t CIA 1 PROGRAM ")
n=int(input("\n\t\t\t Enter no of elements :"))
print("\t\t\t Enter elements : ")
for i in range(n):
    e=input("\t\t\t ")
    li.append(e)
l=[]
for i in li:
        if i[0] in i[1:]:
            l.append(i)       
print("\t\t\t List given : ", li)
print("\t\t\t List modified : ", l)