# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:31:34 2020

@author: James
"""
from functions import pretify_soup, find_hrefs, find_notes_href, webtable_to_pandas, multiple_webtables_to_pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_Irish_counties_by_population'
#page variable from HTML request
source = requests.get(url).text
#create a BeautifulSoup object referencing page variable
soup = BeautifulSoup(source, 'lxml')


#local HTML file
with open("index.html") as fp:
    local_soup = BeautifulSoup(fp, 'lxml') 
    

#Main menu with choices
while True:
    main_choice = int(input("Choose your file to scrape: \n 1: Local HTML \n 2: Website \n 3: Exit Program"))
    #Exit program
    if main_choice == 3:
        break
    
    #Local HTML data scrape
    elif main_choice == 1:
        choice_l = int(input("Would you like to get the \n 1: notes hyperlinks \n 2: all hyperlinks \n 3: Exit Program"))      
        if choice_l == 3:
            break
        elif choice_l == 1:
            print("The hyperlinks are", find_notes_href(soup))
        elif choice_l == 2:
            print("notes hyperlink is", find_hrefs(local_soup))
            
     
    #Web HTML scrape
    elif main_choice == 2:       
        choice = int(input(" \n 1: notes to csv \n 2: webpage to csv \n 3: Exit Program"))   
        if choice == 3:
            break
        elif choice == 1:
            print("Webtable to csv", webtable_to_pandas(soup))
            print("Notes from site was formatted then written to local Webtable.csv")
        elif choice == 2:
            print("Webpage to csv", multiple_webtables_to_pandas())
            break
        else:
            print("invalid choice")
            break
    else:
        print("invalid choice")
        break



































#create csv with table from site
#multiple_webtables_to_pandas()

#drop the unwanted columns
#data_new = dataframe.drop(["Density (km²)","Traditional province","Change since previous census"], axis = 1)
#print(data_new)


#pandas_table = webtable_to_pandas(soup)
#pandas_table.to_csv("Webtable.csv")

#collect all row data and add to list
# =============================================================================
# rows = soup.find_all('tr')
# list_countries =[]
# for row in rows:
#     row_v = row.get_text()
#     list_countries.append(row_v)
# 
# #create pandas dataframe from list
# list_of_countries = pd.DataFrame(list_countries)
# print(list_of_countries.head(20))
# =============================================================================


# =============================================================================
# try:
#     with open("FileOutput.txt", "w") as output:
#         output.write(f"The notes links are: {find_notes_href(soup)}")
#         output.write(f"\n All the links are: {find_hrefs(soup)}")
#             
#         output.close()
# except FileNotFoundError:
#     print("Error,", output," does not exist")
# 
# 
# 
# =============================================================================
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
# status = requests.get(url)
# print(status.status_code)
# 
# =============================================================================
      