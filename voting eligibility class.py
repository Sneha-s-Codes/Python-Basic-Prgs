# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:35:54 2022

@author: sneha
"""

import datetime
class person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(self.dob.year,self.dob.month,self.dob.day):
            print(" INVALID DOB ")
        if age>=18:
            print("\n\t\t\t\t\t You are Eligible to Vote. (Age :  ", age,")")
        else:
            print("\n\t\t\t\t\t You are Not Eligible to Vote. (Age :  ", age,")")
while True:
    print("\n\n\n\n\n\t\t\t\t\t VOTING ELIGIBILITY")
    print("\t\t\t\t\t ------------------")
    name=input("\n\t\t\t\t\t Enter the Name : ")
    year=int(input("\n\t\t\t\t\t Enter the year : "))
    month=int(input("\n\t\t\t\t\t Enter the month : "))
    day=int(input("\n\t\t\t\t\t Enter the day : "))
    p1=person(name,datetime.date(year,month,day))
    p1.check()
    if input("\n\n\n\t\t\t\t\t Do you want to continue :")!='y':
        print("\n\n\n\t\t -----------------------------------------------------------------")
        break
    



