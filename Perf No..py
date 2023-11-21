# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:24:41 2022

@author: Admin
"""

print("\n\n\n\n\n\t\t\t\t\t\t PERFECT NUMBER")
print("\t\t\t\t\t\t --------------")
while True:
    num=int(input("\n\n\t\t\t Enter the number to be checked : "))
    sum=0
    for i in range(1,num):
        if(num%i)==0:
            sum=sum+i
              
          
             
    if num==sum:
        print("\n\t\t\t  is a Perfect Number.", num)
    else:
        print("\n\t\t\t {0} is not a Perfect Number.".format(num))
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
            break
