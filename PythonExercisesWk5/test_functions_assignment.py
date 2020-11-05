# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:04:24 2020

@author: James
"""
from calculations_functions import calc_mean

def test_calc_mean():
    assert calc_mean([1,2,3]) == 2
    assert calc_mean([4,2,3,3]) == 3
