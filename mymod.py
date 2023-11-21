# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:12:05 2022

@author: sneha
"""

def books (l):
    print(l)
    b=input("book to be searched? : ")
    if b in l :
        print(b+" is there in list")
    else:
        print(b+" is not there in the list")