# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:21:32 2020

@author: James
"""
print("Program to analyse the Hits Per Day of the top 10 Linux Distributions")

count = 0
hits_list = []
values_num = int(input("How many values? "))

while count < values_num:
    hits_per_day = int(input("Enter The Hits Per Day: "))
    hits_list.append(hits_per_day)
    count += 1

print("Number of distributions: ", len(hits_list))

hits_list.sort(reverse = True)
print("Hits per day, highest to lowest : ")
for hits_per_day in hits_list:
    print(f"{hits_per_day:>4}")

print("Total hits per day: ", sum(hits_list))
print(f"Average hits per day:  {sum(hits_list) / values_num:.1f}")

# median is the value at the middle index, for an odd number of values
# or the average of the 2 middle values, for an even number
middle_index = int(len(hits_list)/2)

if len(hits_list) %2 == 1: # oddnumber
    print(f"Median hits per day: {hits_list[middle_index]}")
else:
    median = sum(hits_list[middle_index-1:middle_index+1])/2
    print(f"Median hits per day: {median:.1f}")
    
print("Maximum hits per day: ", max(hits_list))
print("Minimum hits per day: ", min(hits_list))