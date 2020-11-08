# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:16:43 2020

@author: James
"""
from math import sqrt

#mean calculation
def calc_mean(values):
    """
    

    Parameters
    ----------
    values : list
        The list of values.

    Returns
    -------
    result : float
        The mean of the values.

    """
    result = sum(values) / len(values)
    return result

#calculate standard devition
def calc_sdv(values, mean):
    """
    

    Parameters
    ----------
    values : list
        The list of values.
    mean : float
        The mean.

    Returns
    -------
    standard_deviation : float
        The standard deviation of a list.

    """
    var = sum(pow(num - mean, 2) for num in values) / len(values) #variance
    standard_deviation = sqrt(var)
    return standard_deviation

