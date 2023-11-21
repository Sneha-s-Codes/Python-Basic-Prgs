# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:02:38 2022

@author: 19bit41
"""

print("\n\n\n\t\t\t\t ODD AND EVEN NO. IN A LIST")
print("\t\t\t\t --------------------------")
while True:
    no=[]
    oddl=[]
    evenl=[]
    n=int(input("\n\n\t\t\t Enter the no. of elements to be in the list : "))
    print("\n\t\t\t\t\t Enter the elements  : ")
    for i in range(n):
        a=int(input("\t\t\t\t\t\t\t\t "))
        no.append(a)

    for i in no:
        if(i%2==0):
            evenl.append(i)

            
        else:
            oddl.append(i)

    print("\n\n\t\t\t\t\t\t Odd List : ")
    
    print("\t\t\t\t\t\t\t\t ", oddl)

    print("\n\n\t\t\t\t\t\t Even List : ")
    
    print("\t\t\t\t\t\t\t\t ", evenl)
    if input("\n\n\t\t\t\t\t\t Do you want to continue? : ")!='y':
        print(".................................................................")
        break
    else:
        print(".................................................................")

        