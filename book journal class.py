# -*- coding: utf-8 -*-
"""
Created on Thu May  5 13:20:53 2022

@author: sneha
"""

class book_journal:
    def __init__(self,b1,j1):
        self.b1=b1
        self.j1=j1
    def avail_book(self,b1):
        book_name= input("\n\t\t\t Enter Book Name : ")
        if book_name in b1:
            print("\n\t\t\t The book is Available")
        if book_name not in b1:
            print("\n\t\t\t The Book Is Not Available")
    def avail_journal(self,j1):
        journal_name=input("\n\t\t\t Enter Journal Name :")
        if journal_name in j1:
            print("\n\t\t\t The book is available")
        if journal_name not in j1:
            print("\n\t\t\t The Book is Not available")
print("\n\t\t\t CHECKING BOOKS AND JOURNAL AVAILABILITY ")
print("\t\t\t --------------------------------------- ")
b1=[]
n=int(input("\n\t\t\t Enter No .Of Books : "))
print("\n\t\t\t Enter Books : ")
for i in range(n):
    b=input("\t\t\t ")
    b1.append(b)
print("\n\t\t\t BOOKS : ",b1)
    
j1=[]
n=int(input("\n\t\t\t Enter No .Of journals : "))
print("\n\t\t\t Enter Journals : ")
for i in range(n):
    j=input("\t\t\t ")
    j1.append(j)
print("\n\t\t\t JOURNALS : ",j1)
p1=book_journal(b1,j1)
while True:
    print("\n\n\n\t\t\t MENU : ")
    print("\t\t\t ------")
    print("\n\t\t\t 1. Books \n\t\t\t 2.Journals ")
    ch=input("\n\t\t\t Enter The Choice :")
    if ch=="1":
        p1.avail_book(b1,j1)
    elif ch=="2":
        p1.avail_journal(j1)
        if input("\n\n\n\t\t\t\t Do you want to continue : ")!='y':
            print("----------------------------------------------------------------------------------")
            break
        