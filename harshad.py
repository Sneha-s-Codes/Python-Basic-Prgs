# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:56:15 2022

@author: 19bit41
"""

print("\n\n\n\t\t\t HARSHAD NO. CHECKING")
print("\t\t\t --------------------")
while True:
    num=int(input("\n\n\t\t\t Enter a number to be checked : "))
   
    
    rem=sum=0
    op=num
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
        
    
    if op%sum==0:
        print("\n\n\t\t\t "+str(op)+" is a Harshad No.")
    else:
        print("\n\n\t\t\t "+str(op)+" is not a Harshad No.")
    
    if input("\n\n\n\t\t\t Do you want to continue? : ")!='y':
        break
    print("\n\t-------------------------------------------------")