# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:21:41 2022

@author: 19bit41
"""


def happyn(num):
    rem=0
    sum=0
    
    while (num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum


print("\n\n\n\t\t\t HAPPY NUMBER ")
print("\t\t\t ------------ ")
while True:
    num=int(input("\n\n\t\t\t Enter a Number : "))
    result=num
    
    
    while(result!=1 and result!=4):
        result=happyn(result)
        
        
    if(result==1):
        print("\n\n\t\t\t "+str(num)+" is a Happy Number.")

    else:
        print("\n\n\t\t\t "+str(num)+' is not a Happy Number.')
    if input("\n\n\n\t\t\t Do you want to continue? : ")!='y':
        break
    print("\n\t-------------------------------------------------")