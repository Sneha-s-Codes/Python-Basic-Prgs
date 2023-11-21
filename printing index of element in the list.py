# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:12:45 2022

@author: sneha
"""

l=[]
print("\n\n\n\t\t\t FINDING INDEX OF A SPECIFIED ELEMENT IN A LIST ")
n=int(input("\n\n\n\t\t\t Enter the size of list : "))
print("\n\n\n\t Enter elements : ")
for i in range(n):
    ele=input(" ")
    l.append(ele)
    
e=input("\n\t\t\t Enter the element to be searched : ")
for j in l:
    if (e in l):
        print("\n\n\n\t\t\t\t Index  :   ["+str(l.index(e))+"] ")
        break
    else:
        print("\n\n\n\t\t\t\t Not in list!")
        break
    