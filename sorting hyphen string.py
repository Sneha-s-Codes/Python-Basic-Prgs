# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:47:18 2022

@author: sneha
"""
while True:
    def hyphen(items):
        items.sort()
        str="-".join(items)
        return str
    print("\n\n\n\t\t\t SORTING HYPHEN SEPERATE WORDS USING FUNCTIONS ")    
    print("\t\t\t --------------------------------------------- ")    

    items=[n for n in input("\n\n\t\t\t Enter the string : ").split('-')]
    
    print("\n\n\t\t\t The strings after sorting  :  ", hyphen(items))

    if input("\n\n\n\n\n\n\t\t\t Do you wanna continue? : ")!='y':
        print("\n\t\t\t ---------------------------------------------------")
        break

