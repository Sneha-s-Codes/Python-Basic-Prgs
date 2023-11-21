# -*- coding: utf-8 -*-
"""
Created on Tue May 10 06:25:45 2022

@author: sneha
"""

class count:
    def __init__(self,str1):
        self.str1=str1
    def upp(self):
        upp=0
        for i in self.str1:
            if i.isupper():
                upp=upp+1
        print("\n Number of uppercase letters : ",upp)
    def spaces(self):
        sp=0
        for i in range(0,len(self.str1)):
            if self.str1[i] in(' '):
                sp=sp+1
        print("\n Number of spaces : ",sp)
    def vow(self):
        vow=0
        self.str1.lower()
        for i in range(0,len(self.str1)):
            if self.str1[i] in ('a','e','i','o','u'):
                vow=vow+1
        print("\n Number of vowels : ",vow)
    def con(self):
        con=0
        self.str1.lower()
        for i in range(0,len(self.str1)):
            if self.str1[i] not in ('a','e','i','o','u'):
                con=con+1
        print("\n Number of consonants : ",con)
print("\n\n\t\t\t\t\t\t COUNTING THE UPPERCASE,SPACES,VOWELS AND CONSONANTS")
print("\t\t\t\t\t\t ---------------------------------------------------")
print("\n 1.COUNT THE UPPERCASE")
print("\n 2.COUNT THE SPACES")
print("\n 3.COUNT THE VOWELS")
print("\n 4.COUNT THE CONSONANTS")
st=input("\n\n Enter the string : ")
p1=count(st)
while True:
    ch=input("\n Enter your choice : ")
    if ch=='1':
        p1.upp()
    elif ch=='2':
        p1.spaces()
    elif ch=='3':
        p1.vow()
    elif ch=='4':
        p1.con()
    if input("\n Do you want to continue : ")!='y':
        break