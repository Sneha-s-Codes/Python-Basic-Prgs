# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:15:00 2022

@author: 19bit41
"""

print("\n\n\n\t\t\t\t POSITIVE AND NEGATIVE NO. IN A TUPLE")
print("\t\t\t\t ------------------------------------")
t=tuple()
p=list()
nq=list()
n=int(input("\n\n\t\t\t Enter the no. of elements to be in the tuple : "))
for i in range(n):
    a=int(input("\n\t\t\t Enter the elements  : "))
    t=t+(a,)
l=list(t)
for i in l:
    if(i>0):
        
        p.append(i)
po=tuple(p)
print("\n\n\t\t\t Positive Tuple : ",po) 

for i in l:
    if(i<0):
        nq.append(i)
ne=tuple(nq)
print("\n\n\t\t\t Negative Tuple : ",ne)    



    
    
