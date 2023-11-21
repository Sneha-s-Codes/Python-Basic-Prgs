# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:06:15 2022

@author: sneha
"""

print("\n\n\t\t\t\t CHARACTER SUBSTITUTED WITH '$' EXCEPT FIRST OCCURANCE ")
s=input("\n\n\n\t\t\t Enter a String : ")
first = s[0]
s1=s.replace(first,"$")
s1=first+s1[1:]
print(s1)

