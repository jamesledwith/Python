# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:16:43 2020

@author: James
"""
from math import sqrt

#mean calculation
def calc_mean(values):
    """
    Student:A00196141

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
    Student:A00196141

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
    Student:A00196141

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
            mode = max_frequency
            max_frequency_list.append(num)
            mode = num
    return mode

#calculate the minimum
def calc_min(list_values):
    """
    Student:A00196141

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
    Student:A00196141

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
    """
    Student:A00196141

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    median : float
        The median value in a list.

    """

    #median of tenure
    list_values.sort()
    mid_index = int(len(list_values)/2)   
    if len(list_values) % 2 == 1:
        median = list_values[mid_index]
        return median
    else:
        median = (list_values(list_values[mid_index -1 ] + list_values[mid_index + 1])/2)
        return median

#calculate the median skewness
def calc_median_skewness(list_values):
    """
    Student:A00196141

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    median_skewness : float
        The median skewness of a list.
    """
    #calculate mean
    mean = sum(list_values) / len(list_values)
    
    #calculate median
    sorted_list = list_values.sort()
    mid_index = int(len(sorted_list)/2)   
    if len(sorted_list) % 2 == 1:
        median = sorted_list[mid_index]
    else:
        median = (sorted_list(sorted_list[mid_index -1 ] + sorted_list[mid_index + 1])/2)
   
    #standard_deviation
    var = sum(pow(num - mean, 2) for num in list_values) / len(list_values) #variance
    standard_deviation = sqrt(var)
    
    median_skewness = 3 * (mean - median) / standard_deviation
    return median_skewness

def calc_mode_skewness(list_values):
   """
    Student:A00196141

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    mode_skewness : float
        The mode skewness of a list.
    """
    #calculate mean
   mean = sum(list_values) / len(list_values)
    
    # calculate mode
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
           mode = max_frequency
           max_frequency_list.append(num)
  # mode = int(max_frequency_list)
   
    #standard_deviation
   var = sum(pow(num - mean, 2) for num in list_values) / len(list_values) #variance
   standard_deviation = sqrt(var)
    
   mode_skewness = (mean - mode) / standard_deviation
   return mode_skewness

def convert_list_to_dictionary(list_values):
    """
    Student:A00196141

    Parameters
    ----------
    list_values : list
        The list of values.

    Returns
    -------
    dictionary_value : dictionary
        The dictionary with values.

    """
    dictionary_value = {}
    for i in range(len(list_values)):
        dictionary_value[list_values[i]] = list_values.count(list_values[i])
    return dictionary_value

#calculate churn rate    
def calc_churn_rate(time_period, data_by_churn):
    """
    Student:A00196141

    Parameters
    ----------
    time_period : string
        The time period for analysis.
    data_by_churn : dict
        The dictionary with values.

    Returns
    -------
    churn_rate : float
        The churn rate values in a dictionary.

    """
    # Determine a time period.
    churn_zero_no = data_by_churn[str(time_period)]
    # Determine the number of customers acquired in this time period. 
    customers_kept = churn_zero_no.count("No")   
    # Determine the number of customers lost or churned in this time period. 
    customers_lost = churn_zero_no.count("Yes")
    try:
        # Divide the number of lost customers by the number of acquired customers.
        # Multiply that number by 100%.
        churn_rate = (customers_lost / customers_kept) * 100
    except ZeroDivisionError as error:
        print("Handling run time error: ", error) 
    return churn_rate















# =============================================================================
# if __name__ == "__main__":
#     test_list = [1,1,1,1,6,5]
#     test_list2 = [3,8,19,17,24,27]
#     print("mean ",calc_mean(test_list))
#     print("mode ", calc_mode(test_list))
#     print("median skew ", calc_median_skewness(test_list))
#     print("min ", calc_min(test_list))
#     print("max ", calc_max(test_list))
#     print("median ", calc_median(test_list))
#     print("standard deviation", calc_sdv(test_list))
#     print("standard deviation", calc_mode_skewness(test_list))
# 
# 
# 
# =============================================================================
