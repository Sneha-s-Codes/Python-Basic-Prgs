# -*- coding: utf-8 -*-
"""
Created on Thu May 26 06:26:13 2022

@author: sneha
"""


try:
    a=10
    b=0
    print("a=",a,"\n b=",b)
    print("a/b: ")
    c=a/b
    raise InvalidDivisor("Cant be divided with 0")  # Raise Error
except InvalidDivisor:
    print ("An exception")
    raise 