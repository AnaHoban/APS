# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:09:26 2024

@author: anahoban

Code to build the dataset from the RESULTS_FILES.txt in each folder
"""
#import statements

import pandas as pd
import csv
import os
import warnings
import numpy as np

warnings.filterwarnings('ignore')

#####################################
#SETTING OUTPUT FILENAMES

output_dir = 'C:/Users/anaho/Desktop/research/language/aps/analysis/Data/Processed data/FrenchLab/'
control_filename = output_dir + 'lab_silentData.csv'
aps_filename = output_dir + 'lab_apsData.csv'


#getting files names
#aps
aps_directory = "C:/Users/anaho/Desktop/ANA_APS/aps/"
#aps_directory = "E:/results ana/aps/"
aps_results_files = []
for root, dirs, files in os.walk(aps_directory):
    for name in files:
        if name.endswith((".txt")):
            aps_results_files.append(root + '/' + name)
            
#control
control_directory = "C:/Users/anaho/Desktop/ANA_APS/control/"
#control_directory = "E:/results ana/control/"
control_results_files = []
for root, dirs, files in os.walk(control_directory):
    for name in files:
        if name.endswith((".txt")):
            control_results_files.append(root + '/' + name)
            
aps_keys = list(pd.read_csv(aps_results_files[1],delimiter = '\t').keys())
control_keys = list(pd.read_csv(control_results_files[1],delimiter = '\t').keys())


# create the data set
aps_data = []
control_data = []

for file in aps_results_files:
    data_file = open(file, "r",encoding = 'utf-8')
    data = list(csv.reader(data_file, delimiter="\t"))[1:] #skipping header
    data_file.close()
    aps_data += data

aps_df = pd.DataFrame(aps_data, columns = aps_keys)
# set dtypes for each column
aps_df['SENTENCE_RT'] = aps_df['SENTENCE_RT'].astype(int)
aps_df['PARAPHRASE_RT'] = aps_df['PARAPHRASE_RT'].astype(float)
aps_df['condition'] = aps_df['condition'].astype(int)
aps_df['TRIAL_INDEX[2]'] = aps_df['TRIAL_INDEX[2]'].astype(int)
aps_df['group'] = 'aps'
aps_df = aps_df[aps_df.sentence_type != 'practice']

dic = {'french': "native", 'chinese': "non-native"}
aps_df['speaker'] = aps_df['speech_condition'].replace(dic)


for file in control_results_files:
    data_file = open(file, "r",encoding = 'utf-8')
    data = list(csv.reader(data_file, delimiter="\t"))[1:] #skipping header
    data_file.close()
    control_data += data

control_df = pd.DataFrame(control_data, columns = control_keys)


# set dtypes for each column
control_df['SENTENCE_RT'] = control_df['SENTENCE_RT'].astype(int)
control_df['PARAPHRASE_RT'] = control_df['PARAPHRASE_RT'].astype(float)
control_df['condition'] = control_df['condition'].astype(int)
control_df['TRIAL_INDEX[2]'] = control_df['TRIAL_INDEX[2]'].astype(int)
control_df['group'] = 'control'
control_df = control_df[control_df.sentence_type != 'practice']


#creating the blocks
#separating per block
control_df.loc[control_df['TRIAL_INDEX[2]'] <= 48, 'block'] = 1
control_df.loc[(control_df['TRIAL_INDEX[2]'] > 48) & (control_df['TRIAL_INDEX[2]'] <= 78), 'block'] = 2
control_df.loc[(control_df['TRIAL_INDEX[2]'] > 78) & (control_df['TRIAL_INDEX[2]'] <= 114), 'block'] = 3
control_df.loc[(control_df['TRIAL_INDEX[2]'] > 114), 'block'] = 4

#separating per block
aps_df.loc[aps_df['TRIAL_INDEX[2]'] <= 48, 'block'] = 1
aps_df.loc[(aps_df['TRIAL_INDEX[2]'] > 48) & (aps_df['TRIAL_INDEX[2]'] <= 78), 'block'] = 2
aps_df.loc[(aps_df['TRIAL_INDEX[2]'] > 78) & (aps_df['TRIAL_INDEX[2]'] <= 114), 'block'] = 3
aps_df.loc[(aps_df['TRIAL_INDEX[2]'] > 114), 'block'] = 4


#some tweaks
aps_df.loc[aps_df['sentence_type'] != 'target', 'condition'] = np.nan
control_df.loc[control_df['sentence_type'] != 'target', 'condition'] = np.nan

# Define the dictionary for mapping
mapping_dict = {'chinese': 'non-native', 'french': 'native'}

# Apply the mapping to the 'speech_condition' column
aps_df['speech_condition'] = aps_df['speech_condition'].map(mapping_dict).fillna(aps_df['speech_condition'])


#saving the data files
aps_df.to_csv(aps_filename, header= True, index = False, encoding='latin1')
control_df.to_csv(control_filename, header= True, index = False, encoding='latin1')
pd.concat([aps_df,control_df]).to_csv(output_dir + 'all_lab_data.csv', header= True, index = False, encoding='latin1')


































