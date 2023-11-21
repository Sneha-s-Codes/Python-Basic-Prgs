# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:03:05 2022

@author: brinda
"""
print("\n\n\n\t\t\t DATA OF THE EMPLOYEES AND THIER SALARIES ")
print("\t\t\t ---------------------------------------- ")
data={}
size=int(input("\n\n\t\t\t Enter size : "))
for i in range(size) :
        key=input("\t\t\t Enter Name  : ")
        val=int(input("\t\t\t Enter Salary : "))
        data[key]=val
while True:
    print("\n\n\t\t\t DATA :  ")
    print("\n\t\t\t\t ", data)
    print("\n\n\t\t\t MENU : ")
    print("\t\t\t ------")
    user_input = input('\n \n\t\t\t 1. Add \n\t\t\t 2. Remove \n\t\t\t 3. Search \n\t\t\t 4. Print  \n\n\t\t\t What Do You Want With This Data: '.title())
    if user_input=='4':
      print("\n\n")
      for key,values in data.items():
        print("\n\t\t\t ",key,'==>',values)
    elif user_input == '1':
      new_name = input('\n\t\t\t Enter A Name Of New Employee : ')
      if new_name in data.keys():
        print('\n\t\t\t This Name Is Already In Data')
      else:
        new_sal = int(input('\n\t\t\t Enter The Salary Of Employee : '))
        data[new_name]=new_sal
        for j in data.items():
          print("\n\t\t\t"+j[0],'==>',j[1])
    elif user_input == '2':
      rem = input('\n\t\t\t Enter A Employee Name To Remove : ')
      if rem in data:
        del data[rem]
        for k in data.items():
          print("\n\t\t\t"+k[0],'==>',k[1])
      else:
        print('\n\t\t\t Employee Does Not Exist')
    elif user_input == '3':
      quer = input('\n\t\t\t Enter The Name Of The Employee Wants To Query : ')
      if quer in data:
        print("\n\n\t\t\t ", data[quer])
      else:
        print('\n\t\t\t The Name Does Not Exist')
    else:
      print('\n\t\t\t Enter Only Valid Input')
      
    if input("\n\n\n\n\n\t\t\t Do you wanna continue? : ")!='y':
          print("\n\n\t\t\t ------------------------------------------------------------------")
          break