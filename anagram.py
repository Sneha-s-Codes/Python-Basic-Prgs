# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:20:50 2022

@author: Admin
"""

print("\n\n\n\t\t\t ANAGRAM CHECKING ")
print("\t\t\t ----------------")
while True:
    s1=input('\n\t\t\t Enter string 1 : ')
    s2=input('\t\t\t Enter string 2 : ')
    o1=s1
    o2=s2
    s1=s1.lower()
    s2=s2.lower()
    if(len(s1)==len(s2)):
        sts1=sorted(s1)
        sts2=sorted(s2)
        if(sts1==sts2):
            print("\n\n\t\t\t The given strings are ANAGRAM.")
        else:
            print("\n\n\t\t\t The given strings are NOT ANAGRAM.")
            
    print("\t\t\t (Entered Strings : "+o1+ " ; "+o2+")")
    if input("\n\n\n\n\t\t\t Do you want to continue? :") != 'y':
        break

