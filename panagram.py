# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:31:27 2022

@author: Admin
"""

def pana(str):
    alph="abcdefghijklmnopqrstuvwxyz"
    for char in alph:
        if char not in str.lower():
            return False
    return True
print("\n\n\n\t\t\t PANAGRAM CHECKING") 
print("\t\t\t -----------------")
while True:
    s=input("\n\t\t\t Enter a sentence to check : ")
    if(pana(s)==True):
        print("\n\t\t\t The given string ("+s+") is a PANAGRAM.")
    else:
        print("\n\t\t\t The given string ("+s+") is NOT a PANAGRAM.") 
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break    
   
        
    
            