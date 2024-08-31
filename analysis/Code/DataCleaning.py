# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:16:21 2024

@author: anahoban

Cleaning the behavioral data
Input: the data set file, which will be one of the following:
        
"""

import functions_preprocessing as func
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import os
import math

#import the df
print('data file to clean:')
data_file = input()
df = pd.read_csv(data_file, encoding = 'latin1')

len_og = len(df)


print('STARTING DATA CLEANING')

#cleaning the sentence reading times for each participant in each condition
print('STATS BEFORE CLEANING', df.SENTENCE_RT.describe())
upper_rt = 16500 
lower_rt = 1000 

clean_df = df[df.SENTENCE_RT < upper_rt]
clean_df = clean_df[clean_df.SENTENCE_RT > lower_rt]

# cutting the values
df.loc[df.SENTENCE_RT > upper_rt, 'SENTENCE_RT'] = np.nan #upper_rt
df.loc[df.SENTENCE_RT < lower_rt, 'SENTENCE_RT'] = np.nan #lower_rt

df = df.dropna(axis = 0, subset = ['SENTENCE_RT']) #remove what is out of the bounds

#for each condition, RTs that were further than 2 std from the mean were removed
clean_df = df
clean_df['log_RT'] = clean_df.SENTENCE_RT.apply(math.log)
#f = open(data_file + '_cleaning.txt', 'w')

print('STARTING DATA CLEANING')

#for each condition, RTs that were further than 2 std from the mean were removed
clean_df = df
clean_df['log_RT'] = clean_df.SENTENCE_RT.apply(math.log)

#scale and remove data that is outside bounds for every condition
for ID in list(clean_df.Session_Name_.unique()):
    for i in [1,2,3,4]: #clean for every condition seperately   
        # Apply scaling to the 'log_RT' column for the specific session and condition
        mask = (clean_df['Session_Name_'] == ID) & (clean_df['condition'] == i)
        clean_df.loc[mask, 'scaled_RT'] = func.scaling(clean_df.loc[mask, 'log_RT'])
        
        # Remove data that is further than 2 standard deviations away from the mean
        mean  = clean_df.loc[mask, 'scaled_RT'].mean()
        std_dev = clean_df.loc[mask, 'scaled_RT'].std()
        lower_bound = mean - 2 * std_dev
        upper_bound = mean + 2 * std_dev
        
        # Replace values below the lower bound with the lower bound
        clean_df.loc[mask & (clean_df['scaled_RT'] < lower_bound), 'scaled_RT'] = lower_bound

        # Replace values above the upper bound with the upper bound
        clean_df.loc[mask & (clean_df['scaled_RT'] > upper_bound), 'scaled_RT'] = upper_bound
        
print('STATS AFTER CLEANING', df.SENTENCE_RT.describe())


print( '% removed by hard bounds:', (1-len(clean_df)/len_og) * 100)

#save the resulting file

# Get the directory path
path = os.path.dirname(data_file)
# Get the file name
file_name = os.path.basename(data_file)

print('There are {} participants'.format(len(clean_df.Session_Name_.unique())))

clean_df.to_csv(path + '/CLEAN_' + file_name , header= True, index = False, encoding='latin1')