# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:52:20 2022

@author: sneha
"""
def avg(l1):
    s=len(l1)
    avg=(sum(l1))/s
    print ("\n\n\n\t\t\t Average : ", avg)
while True:
    li=[]
    print("\n\n\n\n\n\t\t\t FINDING AVERAGE USING FUNCTIONS")
    print("\t\t\t -------------------------------")
    n=int(input("\n\n\t\t\t Enter no. of elements  : "))
    print("\n\t\t\t Enter elements : ")
    for i in range(n):
        e=int(input("\t\t "))
        li.append(e)
    avg(li)
    if input("\n\n\n\n\t\t Do you wanna continue? : ")!='y':
        print("\n\t\t -----------------------------------------------")
        break