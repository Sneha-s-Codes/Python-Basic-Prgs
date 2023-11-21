# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:14:35 2022

@author: sneha
"""

import mymod as book

li=[]
n=int(input(" enter total no. of books : "))
for i in range(n):
    e=input(" enter book names : ")
    li.append(e)
    
book.books(li)