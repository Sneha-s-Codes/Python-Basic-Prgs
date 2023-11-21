# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:16:03 2022

@author: sneha
"""

def ufunc(l):
    dup=[]
    uni=[]
    for i in l:
        
        if i not in dup:
            dup.append(i)
            uni.append(i)
        else:
            continue
    print("\n\n\t\t\t UNIQUE ELEMENTS   :  ", uni)
while True:
    print("\n\n\n\n\t\t\t\t PRINTING UNIQUE VALUES USING A FUNCTION ")
    print("\t\t\t\t --------------------------------------- ")
    li=[]
    n=int(input("\n\n\n\t\t\t Enter the no. of elements  : "))
    print("\n\t\t\t Enter the elements  : ")
    for i in range(n):
        ele=input("\t\t\t\t")
        li.append(ele)
    ufunc(li)
    if input("\n\n\n\t\t\t Do you wanna continue?  :  ")!='y':
        print("\n\n\t\t\t -------------------------------------------------------")
        break
       
