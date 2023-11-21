# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:12:01 2022

@author: 19bit41
"""

print("\n\n\n\t\t\t DISARIUM NO. CHECKING")
print("\t\t\t ---------------------")
while True:
    
    
    num=int(input("\n\n\t\t\t Enter a number to be checked : "))
    len1=len(str(num))
    temp=num
    rem=s=0
    
    while(temp>0):
        rem=temp%10
        s=s+int(rem**len1)
        temp=temp//10
        len1-=1
    
    if(s==num):
        print("\n\n\t\t\t "+str(num)+" is a Disarium No.")
    else:
        print("\n\n\t\t\t "+str(num)+" is not a Disarium No.")
    
    
    if input("\n\n\n\t\t\t Do you want to continue? : ")!='y':
        break
    print("\n\t-------------------------------------------------")