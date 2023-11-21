# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:54:36 2022

@author: sneha
"""
while True:
    def ci(p,r,t):
        c=p*(pow((1+r/100),t))
        print("\n\n\t\t\t Compound Intrest  :  ", c)
 

    print("\n\n\n\t\t\t COMPOUND INTREST CALCULATION USING FUNCTION ")
    print("\t\t\t ------------------------------------------- ")
    p=float(input("\n\n\t\t\t Enter Principle Amount  : "))
    t=int(input("\t\t\t Enter Time (in yrs)  : "))
    r=float(input("\t\t\t Enter Rate of Intrest   : "))
    ci(p,r,t)
    if (input("\n\n\n\n\t\t\t Do you wanna continue? :  ") !='y'):
        print("\n\n\t\t --------------------------------------------------------")
        break
