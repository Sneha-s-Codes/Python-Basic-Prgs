# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:04:16 2022

@author: sneha
"""
while True:
    print("\n\n\n\t\t\t ADDING VALUES OF SAME KEYS IN DICTIONARY ")
    print("\t\t\t ---------------------------------------- ")
    print("\n\n\t\t\t Dictionary - 1 : ")
    d={}
    size=int(input("\n\n\t\t\t Enter size : "))
    for i in range(size) :
            key=input("\t\t\t Enter Key  : ")
            val=int(input("\t\t\t Enter Values : "))
            d[key]=val


    print("\n\n\t\t\t Dictionary - 2 : ")
    di={}
    size=int(input("\n\n\t\t\t Enter size : "))
    for i in range(size) :
            key=input("\t\t\t Enter Key  : ")
            val=int(input("\t\t\t Enter Values : "))
            di[key]=val
    print("\n\n\n\t\t\t Dictionary 1 :", d)
    print("\n\n\n\t\t\t Dictionary 2 :", di)
    
    d3 = {}
    for i, j in d.items():
        for x, y in di.items():
            if i == x:
                d3[i]=int(j+y)
   
    print("\n\n\t\t\t RESULTANT DICTIONARY: ", d3)		
    if input("\n\n\t\t\t Do you wanna continue? : ")!='y':
        print("\n\n\t\t\t ------------------------------------------------")
        break






