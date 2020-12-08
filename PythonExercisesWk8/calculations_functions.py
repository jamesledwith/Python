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
def calc_sdv(values):
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
    mean = calc_mean(values)
    var = sum(pow(num - mean, 2) for num in values) / len(values) #variance
    standard_deviation = sqrt(var)
    return standard_deviation

#calculate the mode
def calc_mode(list_values):
    """
    

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    max_frequency_list : list
        The mode number in a list.

    """
    # the frequency a number appears in a list
    frequency = {}
    for num in list_values:
        frequency.setdefault(num, 0)
        frequency[num] += 1
    # the highest occuring numbers 
    max_frequency = max(frequency.values())
    max_frequency_list = []
    # add highest frequencys to list
    for num, freq in frequency.items():
        if freq == max_frequency:
            max_frequency_list.append(num)
    return max_frequency_list

#calculate the minimum
def calc_min(list_values):
    """
    

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    minimum : float
        The minimum value in  list.

    """
    minimum = min(list_values)
    return minimum

#calculate the maximum
def calc_max(list_values):
    """
    

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    maximum : float
        The maximum value in a list.

    """
    maximum = max(list_values)
    return maximum

#calculate the median
def calc_median(list_values):
    list_values.sort()
    if len(list_values) % 2 ==1:
        return list_values[len//2]
    else:
        return (list_values[len(list_values)//2-1] + list_values[len(list_values)//2])/2
# =============================================================================
#     #median of tenure
#         list_values.sort()
#         mid_index = int(len(list_values)/2)   
#         if len(list_values) % 2 == 1:
#             median_even = list_values[mid_index]
#             return median_even
#         else:
#             median_odd = (list_values(list_values[mid_index -1 ] + list_values[mid_index + 1])/2)
#             return median_odd
# =============================================================================
            
#calculate the median skewness
def calc_median_skewness(list_values):
    mean = calc_mean(list_values)
    median = calc_median(list_values)
    standard_deviation = calc_sdv(list_values)
    median_skewness = 3 * (mean - median) / standard_deviation
    return median_skewness

def calc_mode_skewness(list_values):
    mean = calc_mean(list_values)
    mode = calc_mode(list_values)
    standard_deviation = calc_sdv(list_values)
    mode_skewness = (mean - mode) / standard_deviation
    return mode_skewness


if __name__ == "__main__":
    test_list = [1,1,1,1,6,5]
    print("mean ",calc_mean(test_list))
    print("mode ", calc_mode(test_list))
    print("median skew ", calc_median_skewness(test_list))
    print("min ", calc_min(test_list))
    print("max ", calc_max(test_list))
    print("median ", calc_median(test_list))
    print("standard deviation", calc_sdv(test_list))