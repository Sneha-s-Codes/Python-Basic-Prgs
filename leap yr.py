# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:47:43 2022

@author: 19bit41
"""

print("\n\n\n\t\t\t\t\t LEAP YEAR CHECKING ")
print("\t\t\t\t\t ------------------ ")
while True:
    def ly(yr):
        if(yr%100 !=0 and yr%4==0 and yr%400 !=0):
            print("\n\t\t\t\t\t "+str(yr)+" is a Leap year.")
        else:
            print ("\n\t\t\t\t\t "+str(yr)+" is not a Leap year.")

    y=int(input("\n\t\t\t\t\t Enter a year  : "))
    ly(y)
    
    if input("\n\n\t\t\t\t\t Do you want to continue? : ")=='y':
        print("\n\n\n\t-------------------------------------------------------------------------------")
    else:
        print("\n\n\n\t-------------------------------------------------------------------------------")
        break

    
