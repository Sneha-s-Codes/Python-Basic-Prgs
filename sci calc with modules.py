# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:44:51 2022

@author: sneha
"""

import scicalcimod as calc

n=int(input("\n\t\t\t Enter number of Inputs : "))
if n==1:
    x= int(input("\n\t\t\t Enter the value  : "))
elif n==2:
    a=int(input("\n\t\t\t Enter the value a  : "))
    b=int(input("\t\t\t Enter the value b  : "))
while True:
    print("\n\n\n\t\t\t MENU : ")
    print("\t\t\t ------ ")
    print("\n\t\t\t 1. Add  \n\t\t\t 2. Subtract \n\t\t\t 3. Multiplication \n\t\t\t 4. Division \n\t\t\t 5. Exponent \n\t\t\t 6. Sine \n\t\t\t 7. Cos \n\t\t\t 8. Tan \n\t\t\t 9. Factorial \n\t\t\t 10. Log " )
    ch=int(input("\n\t\t\t Enter Choice :  "))
    if ch==1:
        calc.add(a,b)
    elif ch==2:
        calc.sub(a, b)
    elif ch==3:
        calc.mul(a, b)
    elif ch==4:
        calc.div(a, b)
    elif ch==5:
        calc.exponent(a, b)
    elif ch==6:
        calc.sindegree(x)
    elif ch==7:
        calc.cosdegree(x)
    elif ch==8:
        calc.tandegree(x)
    elif ch==9:
        calc.factorial(x)
    elif ch==10:
        calc.log(x)
    if input("\n\n\n\t\t\t Do you wanna continue  : ")!='y':
        print("\n\t\t\t ---------------------------------------------------------------------------")
        break
