# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:58:25 2022

@author: 19bit41
"""

print("\n\n\n\n\n\n\t\t\t\t\t REMOVING DOTS AND COMMAS IN A STRING ")
s=input("\n\n\t\t\t Enter a string :  ")
news=""
p=".,;?*&"
for i in s:
    if i not in p:
        news=news+i
print("\n\n\t\t\t Output   : ",str(news))