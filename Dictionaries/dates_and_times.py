# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:11:07 2020

@author: james
"""

irish_dict = {1:"A haon",2:"A do",3:"A tri"}
#irish_dict = dict([(1,"A haon"), (2,"A dó"), (3,"A trí")])
length = len(irish_dict)
dict_keys = irish_dict.keys()
values = irish_dict.values()
items = irish_dict.items()
print(items)

	
print({i:i*10 for i in range(1,11)})