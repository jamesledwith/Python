# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:10:09 2020

@author: James
"""
print("This program calculates the download time for a file")

filesize = float(input("Enter the file siz in MB: "));

connectionSpeed = float(input("Enter the connection speed in Mbps: "));
downloadTime = (filesize * 8.388608) / connectionSpeed;
print("Download time is " ,round(downloadTime,2), " seconds");
