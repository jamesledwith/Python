# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:12:01 2020

@author: James
"""
import math

print("This program calculates the limit associated with Network Throughput")

maximumSegmentSize = float(input("Enter the maximun segment size: "))
roundTripTime = float(input("Enter the round-trip time: ")) 
probPacketLoss = float(input("Enter the probability of packet loss: ")) 

limit = (maximumSegmentSize / (roundTripTime * (math.sqrt(probPacketLoss)))) 

print(f"Limit is {limit:.2f}") 
