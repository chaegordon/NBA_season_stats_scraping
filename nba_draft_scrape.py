# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:30:43 2019

@author: chaeg

This is a program to scrape a given url for information and follows the guid by
https://fansided.com/2015/09/07/nylon-calculus-101-data-scraping-with-python/
but for a different url. in a similar way these data frames could be combined
for the sake of machine learning predictions of draft stock.
"""

#import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

#needed to convert unicode to numeric
import unicodedata


url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_poss.html'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')

#index of soup.findall to be adjusted and checked with a print statement
#to make sure right number of columns being passed into df

column_headers = [th.getText() for th in 
                  soup.findAll('tr', limit=2)[0].findAll('th')]

#get rid of the rank thing because it is not in the player_data

column_headers = column_headers[1:]

data_rows = soup.findAll('tr')[1:]  # skip the first 1 header rows

player_data = []  # create an empty list to hold all the data

for i in range(len(data_rows)):  # for each table row
    player_row = []  # create an empty list for each player

    # for each table data element from each table row
    for td in data_rows[i].findAll('td'):        
        # get the text content and append to the player_row 
        player_row.append(td.getText())        

    # then append each pick/player to the player_data matrix
    player_data.append(player_row)
    

#print(column_headers)

df = pd.DataFrame(player_data, columns=column_headers)
df = df[df.Player.notnull()]
df = df.convert_objects(convert_numeric=True)
df = df[:].fillna(0) # index all the columns and fill in the 0s
print(df.dtypes)
# Create a variable with the url
url_template = 'https://www.basketball-reference.com/leagues/NBA_{year}_per_poss.html'

# create an empty DataFrame
draft_df = pd.DataFrame()
for year in range(1978, 2018):  # for each year
    url = url_template.format(year=year)  # get the url
    
    html = requests.get(url)  # get the html
    
    soup = BeautifulSoup(html.text, 'html5lib') # create our BS object, need the TEXT part
    

    # get our player data
    data_rows = soup.findAll('tr')[1:] 
    player_data = [[td.getText() for td in data_rows[i].findAll('td')]
                for i in range(len(data_rows))]
    
    # Turn yearly data into a DatFrame
    year_df = pd.DataFrame(player_data, columns=column_headers)
    # create and insert the Draft_Yr column
    year_df.insert(0, 'Year_stats', year)
    
    # Append to the big dataframe
    draft_df = draft_df.append(year_df, ignore_index=True)
    time.sleep(0.01)
    
draft_df = draft_df[draft_df.Player.notnull()]
draft_df = draft_df.convert_objects(convert_numeric=True)
draft_df = draft_df[:].fillna(0)

draft_df.to_csv('Season_Stats_scraped.csv')




