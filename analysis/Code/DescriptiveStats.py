# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:51:41 2024

@author: anahoban

This file creates the plots for the descriptive stats only for one group

REMINDER:
    COND1 : SRC PLAUSIBLE
    COND2 : SRC IMPLAUSIBLE
    COND3 : ORC PLAUSIBLE
    COND4 : ORC IMPLAUSIBLE

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions_preprocessing as func
import os
import math

print('data file:')
data_file = input()

# Get the directory path
path = os.path.dirname(data_file)
# Get the file name
file_name = os.path.basename(data_file)

print('group?')
group = input()
#data_file = 'clean_only_aps_data.csv'
#data_file = 'clean_only_control_data.csv'

df_all = pd.read_csv(data_file, encoding = 'latin1')

#keeping only correct RTs:
df = df_all[df_all.PARAPHRASE_ACCURACY == 1]


### Reading times ###

# PLOTTING HISTOGRAM OF ALL CONDITIONS
'''
sns.distplot(df.SENTENCE_RT, label = 'all')
sns.distplot(df.loc[df.condition == 1,'SENTENCE_RT'], label = 'cond1')
sns.distplot(df.loc[df.condition == 2,'SENTENCE_RT'], label = 'cond2')
sns.distplot(df.loc[df.condition == 3,'SENTENCE_RT'], label = 'cond3')
sns.distplot(df.loc[df.condition == 4,'SENTENCE_RT'], label = 'cond4')

plt.title(group + ' RT Distribution for each condition')
plt.legend()
'''
# PLOTTING BAR PLOTS TO COMPARE ACROSS CONDITIONS

func.plot_across_conditions(df, 'SENTENCE_RT')
plt.title(data_file)
plt.savefig('../plots/DescriptiveStats/OnlineData/RT_'+ file_name[:-4] +'.png')


### ACCURACY ###

    
#get the number of correct answers for each participant in each condition
#for aps:
if group == 'aps':
    print('aps group')
    summary_df = df.drop_duplicates(subset = ['Session_Name_', 'condition', 'group', 'speech_condition','block','syntactic_condition', 'plausibility_condition']).loc[:,['Session_Name_', 'condition','group','speech_condition','block','syntactic_condition', 'plausibility_condition']]
    summary_df.reset_index(drop=True, inplace=True)
    
    
    for ID in list(df.Session_Name_.unique()):
        for speaker in ['native', 'non-native']:
            for cond in [1,2,3,4]:                
                corr = len(df[(df.Session_Name_ == ID) & (df.condition == cond) & (df.speech_condition == speaker)])
                tot  = len(df_all[(df_all.Session_Name_ == ID) & (df_all.condition == cond) & (df_all.speech_condition == speaker) ])
                
                if tot == 0:
                    ratio = 0
                else: 
                    ratio = corr/tot
                summary_df.loc[(summary_df.condition == cond) & (summary_df.Session_Name_== ID) & (summary_df.speech_condition == speaker), 'PERC_CORRECT'] = ratio
                
#control
if group != 'aps':
    summary_df = df.drop_duplicates(subset = ['Session_Name_', 'condition', 'group','block', 'syntactic_condition', 'plausibility_condition']).loc[:,['Session_Name_', 'condition','group','block','syntactic_condition', 'plausibility_condition']]
    summary_df.reset_index(drop=True, inplace=True)
    
    for ID in list(df.Session_Name_.unique()):
        for speaker in ['native', 'non-native']:
            for cond in [1,2,3,4]:
            
                corr = len(df[(df.Session_Name_ == ID) & (df.condition == cond) ])
                tot  = len(df_all[(df_all.Session_Name_ == ID) & (df_all.condition == cond) ])
                summary_df.loc[(summary_df.condition == cond) & (summary_df.Session_Name_== ID), 'PERC_CORRECT'] = corr/tot

func.plot_across_conditions(summary_df, 'PERC_CORRECT')
plt.title(data_file)
plt.savefig('../plots/DescriptiveStats/OnlineData/ACC_'+ file_name[:-4] +'.png')

#save them


#save the resulting file
df.to_csv(path + '/CORR_' + file_name , header= True, index = False, encoding='latin1')
summary_df.to_csv(path + '/CORR_summary_' + file_name , header= True, index = False, encoding='latin1')

