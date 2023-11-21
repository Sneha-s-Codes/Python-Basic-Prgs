# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:52:40 2022

@author: brinda
"""

from collections import Counter
print("\n\n\t\t\t CALCULATION OF AMOUNT IN DICTIONARIES ")
print("\t\t\t ------------------------------------- ")
item_list = [{'item': 'Pizza', 'amount': 400}, {'item': 'Burger', 'amount': 300}, {'item': 'Pizza', 'amount': 750}]
print("\n\n\t\t\t ITEM LIST : ")
print("\n\t\t\t ", item_list)
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print("\n\n\n\t\t\t TOTAL AMOUNT SPENT : ")
print("\n\t\t\t\t ", result)