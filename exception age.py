# -*- coding: utf-8 -*-
"""
Created on Thu May 26 07:53:16 2022

@author: sneha
"""
import datetime
class MyError(Exception):

    def res(self):
        print(" INVALID AGE")

try:
    
    year=int(input("\n\t\t\t\t\t Enter the year : "))
    today=datetime.date.today()
    age= today.year-year
    if age<35:
        raise(MyError(" AGE ERROR "))
	# Value of Exception is stored in error
except MyError:
	print('\n\n\t\t\t\t\tA New Exception occured: INVALID AGE')

else:
    print("eligible")

