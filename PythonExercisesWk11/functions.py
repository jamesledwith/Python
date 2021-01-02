# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:39:08 2021

@author: James
"""

def pretify_soup(soup):
    return soup.prettify()
    
def find_hrefs(soup):
    #extract links from a site     
    for a in soup.find_all('a', href=True):
        print("Found the Url:", a['href'])