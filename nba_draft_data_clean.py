# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:00:36 2019

@author: chaeg

Taking scraped data and cleaning it and seperating it into a test and train data set

"""

"""# Convert data to proper data types
draft_df = draft_df.convert_objects(convert_numeric=True)

# Get rid of the rows full of null values
draft_df = draft_df[draft_df.Player.notnull()]

# Replace NaNs with 0s
draft_df = draft_df.fillna(0)

# Rename Columns
draft_df.rename(columns={'WS/48':'WS_per_48'}, inplace=True)
# Change % symbol
draft_df.columns = draft_df.columns.str.replace('%', '_Perc')
# Add per_G to per game stats
draft_df.columns.values[15:19] = [draft_df.columns.values[15:19][col] + 
                                  "_per_G" for col in range(4)]

# Changing the Data Types to int
draft_df.loc[:,'Yrs':'AST'] = draft_df.loc[:,'Yrs':'AST'].astype(int)

# Delete the 'Rk' column
draft_df.drop('Rk', axis='columns', inplace=True)"""

import pandas as pd
import numpy as np

