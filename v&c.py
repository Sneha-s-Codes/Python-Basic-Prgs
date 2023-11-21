# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:14:12 2022

@author: Admin
"""

print("\n\n\n\n\n\t\t\t\t\t COUNTING VOWELS & CONSONENTS ")
print("\t\t\t\t\t ---------------------------- ")
while True:
    s=input("\n\n\t\t\t Enter a string : ")
    v=0
    c=0
    b=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            v+=1
        elif i in (" "):
            b+=1
        else:
            c+=1
    print("\n\n\t\t\t GIVEN STRING : %s"%s)
    print("\n\t\t\t VOWELS       : %d"%v)
    print("\t\t\t CONSONENTS   : %d"%c)
    print("blank space : ", b)
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break
    print("\n\t-------------------------------------------------")
