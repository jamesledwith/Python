# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:10:51 2020

@author: James
"""
import numpy as np

# =============================================================================
# a1 = np.array([1,2,3,4,5,6])
# print("type is", type(a1))
# print("length is ", len(a1))
# =============================================================================
 
data = np.loadtxt("wine.csv", delimiter = ",", skiprows = 1)
print("length (rows) is ", len(data))
print("type is", type(data))
print("length of axis 1 (number of culumns ) is", data.shape[1])
print("number of values is", data.size)
print("number of array dimensions are", data.ndim)
r1 = data[5,2] # [row][column]
print("type of row is", type(r1))
chlorides,density,pH,sulphates,alcohol,quality = data.T
print("number of dimensions in quality column is ", quality.ndim)
max_of_quality = quality.max()
#print(len(max_of_quality))
print("maximum of quality column is ", max_of_quality)
min_of_quality = quality.min()
print("minimum of quality column is ", min_of_quality)
mean_of_quality = quality.mean()
print("mean of quality column is ", mean_of_quality)
median_of_quality = np.median(quality)
print("median of quality column is ", median_of_quality)

c1 = np.corrcoef(quality,density)
c2 = np.corrcoef(quality,chlorides)
c3 = np.corrcoef(quality,sulphates)
c4 = np.corrcoef(quality,alcohol)

