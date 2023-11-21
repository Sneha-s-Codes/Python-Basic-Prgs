# -*- coding: utf-8 -*-
"""
Created on Thu May 26 07:47:26 2022

@author: sneha
"""


def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
l=set()
n= int(input("range :"))
for i in range(n):
    e=int(input(""))
    l.add(e)
print(l)
c=int(input(" no. to be checked : "))
print(" RESULT : ",is_group_member(l,c)) 