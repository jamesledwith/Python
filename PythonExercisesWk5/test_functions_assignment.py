# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:04:24 2020

@author: James
"""
from pytest import approx
from calculations_functions import calc_mean, calc_sdv, calc_mode

def test_calc_mean():
    assert calc_mean([1,2,3]) == 2
    assert calc_mean([4,2,3,3]) == 3
    
def test_calc_sdv():
    assert calc_sdv([10, 12, 23, 23, 16, 23, 21, 16] , 18) == approx(4.8989, 0.04)
    assert calc_sdv([234, 5443, 1 ,10, 12, 23, 23] , 820) == approx(1888.52, 0.02)

def test_calc_mode():
    assert calc_mode([1,1,1,2,3,4,5]) == 1
    assert calc_mode([6,6,6,1,2,3,4,5,5]) == 6