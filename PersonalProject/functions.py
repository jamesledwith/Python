# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:39:08 2021

@author: James
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

def pretify_soup(soup):
    return soup.prettify()
    
def find_hrefs(soup):
    """
    

    Parameters
    ----------
    soup : BeautifulSoup Object
        Soup object containing HTML file.

    Returns
    -------
    None.

    """
    #extract links from a site     
    for a in soup.find_all('a', href=True):
        print("Found the Url:", a['href'])
        
        
def find_notes_href(soup):
    """
    

    Parameters
    ----------
    soup : BeautifulSoup Object
        Soup object containing HTML file.

    Returns
    -------
    None.

    """
    #get the list elements
    links = soup.find("ol", attrs = {"class": "references"})
    
    #print each link found
    for a in links.find_all('a', href=True):
            print("Found the Url:", a['href'])
            
            
            
def webtable_to_pandas(soup):
    """
    

    Parameters
    ----------
    soup : BeautifulSoup Object
        Soup object containing HTML file.

    Returns
    -------
    data_new : Dataframe
        The pandas dataframe containing the tables values..

    """
    #get table with class name
    table = soup.find("table", {"class": "wikitable"})
    
    #read table into list of dataframe objects
    dataframe = pd.read_html(str(table))
    #convert the list to a pandas dataframe
    dataframe = pd.DataFrame(dataframe[0])
    
    #drop the unwanted columns
    data_new = dataframe.drop(["Density (km²)","Traditional province","Change since previous census"], axis = 1)
    data_new.to_csv("Webtable.csv")
    return data_new

def webtables_to_csv():
   """
    

    Parameters
    ----------
    soup : BeautifulSoup Object
        Soup object containing a table.

    Returns
    -------
    dataframe : Dataframe
        The pandas dataframe containing the tables values.

    """
   try:
       csv_name = input(str("Name your file: "))
       url = input(str("Please enter your websites URL: "))
    
   except:
       print("Error", url, "cannot be found")
    
   source = requests.get(url).text
   soup = BeautifulSoup(source, 'lxml')
   
   #get table with class name
   table = soup.find("table", {"class": "wikitable"})
    
   #read table into list of dataframe objects
   dataframe = pd.read_html(str(table))
   
   #convert the list to a pandas dataframe
   dataframe = pd.DataFrame(dataframe[0])
   
   #store the dataframe in a local csv file
   dataframe.to_csv(csv_name + ".csv")
   return dataframe

    

   
