# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:31:34 2020

@author: James
"""
from functions import pretify_soup, find_hrefs
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.mapability.com/ei8ic/contest/eicounty.php'
#page variable from HTML request
source = requests.get(url).text

#crete a BeautifulSoup object referencing page variable
soup = BeautifulSoup(source, 'lxml')

#collect all row data and add to list
rows = soup.find_all('tr')
list_countries =[]
for row in rows:
    row_v = row.get_text()
    list_countries.append(row_v)

#create pandas dataframe from list
list_of_countries = pd.DataFrame(list_countries)
print(list_of_countries.head(20))





#print(soup.prettify())

# =============================================================================
# 
# for a in soup.find_all('a', href=True):
#         print("Found the Url:", a['href'])
# 
# =============================================================================
# =============================================================================
# table = soup.find('table')
# #print(table_rows.text)
# table_rows = table.find_all('tr')
# for table_r in table_rows:
#     table_data = table_r.find_all('td')
#     row = [i.text for i in table_data]
#     #for i in table_data:
#         #row = i
#     print(row)
# 
# =============================================================================
dataframes = pd.read_html('https://en.wikipedia.org/wiki/Counties_of_Ireland', header=0)

for dataframe in dataframes:
    print(dataframe)










# =============================================================================
# 
# with open("index.html") as fp:
#     
#     soup = BeautifulSoup(fp, 'lxml')
#     title = soup.title
#     head = soup.head
#     body = soup.body
#     body_paragraphs = soup.body.p
#     all_lists = soup.find_all('li')
#     body_text = soup.body.text
#     search = soup.find('div', class_= 'sidebar')
#     
#     print("Search for ", search)   
#     print("All lists ",all_lists)
#     print("\n Title is ",title)
#     print("\n Head is ",head)
#     print("\n Body's paragraphs are ",body_paragraphs)
#     print("\n Body is ",body)
#     print("\n Body text is ",body_text)
#     
#     #extract links from a site     
#     for a in soup.find_all('a', href=True):
#         print("Found the Url:", a['href'])
#            
#     print(soup.prettify())
#     
#   
# =============================================================================
    
  
    
# =============================================================================
# with open("index.html") as fp:
#     local_soup = BeautifulSoup(fp, 'lxml') 
#     
# 
# while True:
#     main_choice = int(input("Choose your file to scrape: \n 1: Local HTML \n 2: Website \n 3: Exit Program"))
#     
#     #Main menu with choices
#     
#     #Exit program
#     if main_choice == 3:
#         break
#     
#     #Local HTML data scrape
#     elif main_choice == 1:
#         choice_l = int(input("Would you like to get the \n 1: Hyperlinks \n 2: Tables \n 3: Exit Program"))
#         
#         if choice_l == 3:
#             break
#         elif choice_l == 1:
#             print("The hyperlinks are", find_hrefs(local_soup))
#         elif choice_l == 2:
#             #print("The tables are", find_hrefs(local_soup))
#             dfs = pd.read_html('index.html', header = 0)
#             for df in dfs:
#                 print(df)
#      
#     #Web HTML scrape
#     elif main_choice == 2:
#         break
#     
#     else:
#         print("invalid choice")
#         break
# =============================================================================
                
           # =============================================================================
    #                     #Calculate Churn Rate
    #                     elif choice == 9:
    #                         while True:
    #                             churn_choice = int(input("Churn Rate (1)Month (2)Exit"))
    #                             if churn_choice == 1:
    #                                 try:
    #                                     time_period = input("Please enter your timeframe (0-72)")
    #                                     print(f"The churn rate of month {time_period} is, {calc_churn_rate(time_period,data_by_churn):0.02f} %")   
    #                                 except KeyError as error:
    #                                     print("Handling Out of bounds error", error)
    #                             elif churn_choice == 2:    
    #                                 break
    #                             else:
    #                                 print("Please enter a correct value")
    #                     
    #                     else:
    #                         print("Please enter a correct value")
    #             
    # =============================================================================      
            