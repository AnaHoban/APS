# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:40:13 2024

@author: anahoban

for online data control 
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions_preprocessing as func
from prettytable import PrettyTable 
import numpy as np



def produce_table_silent(block = 0):
    myTable = PrettyTable(["Speaker", "Structure", "RT - Plausible", "RT - Implausible", "AC - Plausible", "AC -Implausible"]) 
   
    
    control_final = pd.read_csv("CORR_clean_online_silentData_formatted.csv", encoding = 'latin1')
    control_summary = pd.read_csv("CORR_summary_CLEAN_online_silentData_formatted.csv", encoding = 'latin1')

    #control
    myTable.add_row(["No APS", "SRC", "{mean} ({std})".format(mean = round(control_final.loc[control_final.condition == 1,'SENTENCE_RT'].mean()), std = round(control_final.loc[control_final.condition == 1,'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(control_final.loc[control_final.condition == 2,'SENTENCE_RT'].mean()), std = round(control_final.loc[control_final.condition == 2,'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(control_summary.loc[control_summary.condition == 1 ,'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[control_summary.condition == 1 ,'PERC_CORRECT'].std(),2)),
                                      "{mean} ({std})".format(mean = round(control_summary.loc[control_summary.condition == 2 ,'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[control_summary.condition == 2 ,'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([" ", "ORC", "{mean} ({std})".format(mean = round(control_final.loc[control_final.condition == 3 ,'SENTENCE_RT'].mean()), std =  round(control_final.loc[control_final.condition == 3 ,'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(control_final.loc[control_final.condition == 4 ,'SENTENCE_RT'].mean()), std = round(control_final.loc[control_final.condition == 4 ,'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(control_summary.loc[control_summary.condition == 3 ,'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[control_summary.condition == 3 ,'PERC_CORRECT'].std(),2)),
                                      "{mean} ({std})".format(mean = round(control_summary.loc[control_summary.condition == 4 ,'PERC_CORRECT'].mean(),2),std = round(control_summary.loc[control_summary.condition == 4 ,'PERC_CORRECT'].std(),2)) ])


    myTable.add_row([ " " , " " ," " " "," "," ", " "])
    
    print(myTable)
    
def produce_table_aps(block = 0):
    myTable = PrettyTable(["Speaker", "Structure", "RT - Plausible", "RT - Implausible", "AC - Plausible", "AC -Implausible"]) 
    
    control_final = pd.read_csv("CORR_clean_french_online_apsData_formatted.csv", encoding = 'latin1').drop('Response', axis=1)
    control_summary = pd.read_csv("CORR_summary_clean_french_online_apsData_formatted.csv", encoding = 'latin1')


    # French Speaker
    myTable.add_row(["french", "SRC", 
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 1) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 1) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 2) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 2) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 1) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 1) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].std(),2)),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 2) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 2) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([" ", "ORC", 
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 3) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std =  round(control_final.loc[(control_final.condition == 3) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 4) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 4) & (control_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 3) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 3) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].std(),2)),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 4) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].mean(),2),std = round(control_summary.loc[(control_summary.condition == 4) & (control_summary.speech_condition == 'french'),'PERC_CORRECT'].std(),2)) ])

    # Chinese Speaker
    myTable.add_row(["chinese", "SRC", 
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 1) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 1) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 2) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 2) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 1) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 1) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].std(),2)),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 2) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 2) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([" ", "ORC", 
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 3) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std =  round(control_final.loc[(control_final.condition == 3) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_final.loc[(control_final.condition == 4) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(control_final.loc[(control_final.condition == 4) & (control_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 3) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].mean(),2), std = round(control_summary.loc[(control_summary.condition == 3) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].std(),2)),
                     "{mean} ({std})".format(mean = round(control_summary.loc[(control_summary.condition == 4) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].mean(),2),std = round(control_summary.loc[(control_summary.condition == 4) & (control_summary.speech_condition == 'chinese'),'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([ " " , " " ," " " "," "," ", " "])
    
    print(myTable)

    
produce_table_aps()
