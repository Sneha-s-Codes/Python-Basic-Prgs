# -*- coding: utf-8 -*-
"""
Created on Thu May 26 04:54:50 2022

@author: sneha
"""

print(" ARMSTRONG ")
n=input("number : ")
sum=0
ch=int(n)
for i in n:
    no=int(i)
    sum=sum+(no**3)
print(sum)  
if(ch==sum):
    print("armstrong")