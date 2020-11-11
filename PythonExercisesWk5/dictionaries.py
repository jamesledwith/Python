# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:22:36 2020

@author: james
"""
import time, datetime
#thisdate = datetime.datetime(2020, 11, 6)
#firstdate = datetime.datetime(2020, 11, 9, 9)
nye = datetime.datetime(2021, 1, 1, 0, 0, 0)
time = datetime.datetime(2021, 1, 9,3, 4, 5)
#time = datetime.datetime.time()
#(, , 9,3, 4, 5)
#delta = seconddate - firstdate
delta = nye - time
print(delta)
#print(datetime.datetime.strptime(%A %B %d %H:%M:%S %Z %Y)
#print(datetime.datetime.strptime("11/7/2020", "%d/%m/%Y"))
#datetime.datetime.fromisoformat(%A %B %d %H:%M:%S %Z %Y)