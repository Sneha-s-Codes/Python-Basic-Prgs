# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:19:45 2022

@author: sneha
"""
while True:
    def uplow(st):
        u=0
        l=0
        for i in st:
            if i.isupper():
                u+=1    #u=u+1
            elif i.islower():
                l+=1
            else:
                continue
        print("\t\t\t Upper-Case Characters : ",u)
        print("\t\t\t Lower-Case Characters : ",l)

    print("\n\n\t\t\t COUNTING UPPER AND LOWER IN A STRING USING FUNCTIONS")
    print("\t\t\t ----------------------------------------------------")
    s=input("\n\n\t\t\t Enter a string : ")
    uplow(s)
    if input("\n\n\t\t\t Do you wanna continue? : ")!='y':
        print("\n\n\t\t  -----------------------------------------------------")
        break