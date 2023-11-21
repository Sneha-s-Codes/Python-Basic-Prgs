# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:11:17 2022

@author: 19bit41
"""

print("\n\n\t\t\t\t PRINTING CUBE OF ODDS IN A DICTIONARY")
print("\t\t\t\t ------------------------------------- ")
a=int(input("\n\t\t\t Enter the starting range :"))
b=int(input("\t\t\t Enter the ending range   :"))
myd={ }

for x in range(a,b+1):
    if(x%2!=0):
        myd[x]=x**3
print("\n\t\t\t ",myd)   
    

