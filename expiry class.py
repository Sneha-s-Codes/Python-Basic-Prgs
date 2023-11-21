# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:27:41 2022

@author: sneha
"""

from datetime import *
class expiry():
  def exp(self,ex):
      y=ex.year-date.today().year
      m=ex.month-date.today().month
      d=ex.day-date.today().day
      print("\n\n\n\t\t The remaining year is  ",y)
      print("\t\t The remaining month is ",m)
      print("\t\t The remaining date is   ",d)


obj=expiry()
print("\n\t\t EXPIRY DATE CALCULATION")
print("\t\t +++++++++++++++++++++++")
y=int(input("\n\t\t Enter the year  :"))
m=int(input("\n\t\t Enter the month :"))
d=int(input("\n\t\t Enter the date  :"))
ex=date(y,m,d)
obj.exp(ex)