# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:40:13 2024

@author: anahoban

Comparing controls to aaps
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions_preprocessing as func
from prettytable import PrettyTable 
import numpy as np


#eyetracking data
aps_final = pd.read_csv('CORR_clean_only_aps_data.csv', encoding = 'latin1')
control_final =  pd.read_csv('CORR_clean_only_control_data.csv', encoding = 'latin1')
aps_summary =  pd.read_csv('CORR_summary_clean_only_aps_data.csv', encoding = 'latin1')
control_summary =  pd.read_csv('CORR_summary_clean_only_control_data.csv', encoding = 'latin1')

all_correct_final = pd.concat([aps_final, control_final])
summary_dfs = pd.concat([aps_summary, control_summary])

#all_final.to_csv('all_groups_data.csv', header= True, index = False, encoding='latin1')
all_final = pd.concat([aps_final, control_final])


def get_means2(df, y_to_plot, group):
    mean_cond1 = df.loc[(df.condition == 1) & (df.group == group), y_to_plot].mean()
    mean_cond2 = df.loc[(df.condition == 2) & (df.group == group), y_to_plot].mean()
    mean_cond3 = df.loc[(df.condition == 3) & (df.group == group), y_to_plot].mean()
    mean_cond4 = df.loc[(df.condition == 4) & (df.group == group), y_to_plot].mean()
    
    return mean_cond1, mean_cond2, mean_cond3, mean_cond4

def plot_means2(means, group):
    if group == 'aps':
        mins = [0.05,0.3,0.55,0.8] 
        maxs = [0.12,0.36,0.62,0.86]
    elif group == 'control':
        mins = [0.14,0.40,0.64,0.90]
        maxs = [0.22,0.46,0.70,0.96] 
     
    for i,mean in enumerate(means):
        ax.axhline(mean, xmin = mins[i], xmax = maxs[i], ls='--', color = 'r')
        
    return means


labels = ['subject plausible','subject implausible', 'object plausible','object implausible']
data = all_final
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x='condition', y='SENTENCE_RT', hue="group",  data=data, saturation = 0.5, boxprops={'alpha': 0.4})
sns.stripplot(x='condition', y='SENTENCE_RT', hue = "group", data=data, dodge=True, ax=ax, alpha = 0.5)
plot_means2(get_means2(data, 'SENTENCE_RT', 'aps'), 'aps')
plot_means2(get_means2(data, 'SENTENCE_RT', 'control'), 'control')
fig.set_xticklabels(labels);
fig.set_ylabel('Reading time (log and norm)')
fig.set_title('RTs For All answers')

labels = ['subject plausible','subject implausible', 'object plausible','object implausible']
data = summary_dfs
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x='condition', y='PERC_CORRECT', data=data, hue = 'group', boxprops={'alpha': 0.8})
fig.set_xticklabels(labels);
plot_means2(get_means2(data, 'PERC_CORRECT', 'aps'), 'aps')
plot_means2(get_means2(data, 'PERC_CORRECT', 'control'), 'control')
fig.set_ylabel('Proportion of correct answers')
fig.set_title('Paraphrase Accuracy')


# Specify the Column Names while initializing the Table 
 
# Add rows 

def produce_table1(block = 0):
    myTable = PrettyTable(["Speaker", "Structure", "RT - Plausible", "RT - Implausible", "AC - Plausible", "AC -Implausible"]) 
    
    if block == 0:
        
        control_final = all_correct_final[(all_correct_final.group == 'control')]
        control_summary = summary_dfs[(summary_dfs.group == 'control')]
    
        aps_final = all_correct_final[(all_correct_final.group == 'aps')]
        aps_summary = summary_dfs[(summary_dfs.group == 'aps')]
    
    elif block in [1,2,3,4]:
        control_final = all_correct_final[(all_correct_final.block == block) & (all_correct_final.group == 'control')]
        control_summary = summary_dfs[(summary_dfs.block == block) & (summary_dfs.group == 'control')]
    
        aps_final = all_correct_final[(all_correct_final.block == block) & (all_correct_final.group == 'aps')]
        aps_summary = summary_dfs[(summary_dfs.block == block) & (summary_dfs.group == 'aps')]
    

    
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

    #aps

    myTable.add_row(["APS - FRENCH", "SRC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 1) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std= round(aps_final.loc[(aps_final.condition == 1) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 2) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std= round(aps_final.loc[(aps_final.condition == 2) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 1) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 1) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].std(),2)),
                                      "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 2) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 2) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([" ", "ORC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 3) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 3) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 4) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 4) & (aps_final.speech_condition == 'french'),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 3) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 3) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].std(),2)),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 4) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 4) & (aps_summary.speech_condition == 'french') ,'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([ " " , " " ," " " "," "," ", " "])

    #aps

    myTable.add_row(["APS - CHINESE", "SRC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 1) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 1) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 2) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 2) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                                      "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 1) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 1) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].std(),2)),
                                      "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 2) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 2) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].std(),2)) ])

    myTable.add_row([" ", "ORC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 3) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 3) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 4) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 4) & (aps_final.speech_condition == 'chinese'),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 3) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 3) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].std(),2)),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 4) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 4) & (aps_summary.speech_condition == 'chinese') ,'PERC_CORRECT'].std(),2)) ])
    
    
    #all_aps
    myTable.add_row([ " " , " " ," " " "," "," ", " "])

    myTable.add_row(["APS - ALL", "SRC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 1) ,'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 1) ,'SENTENCE_RT'].std())),
                                         "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 2), 'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 2), 'SENTENCE_RT'].std())),
                                         "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 1), 'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 1), 'PERC_CORRECT'].std(),2)),
                                         "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 2),'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 2),'PERC_CORRECT'].std(),2))  ])

    myTable.add_row([" ", "ORC", "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 3),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 3),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_final.loc[(aps_final.condition == 4),'SENTENCE_RT'].mean()), std = round(aps_final.loc[(aps_final.condition == 4),'SENTENCE_RT'].std())),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 3)  ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 3)  ,'PERC_CORRECT'].std(),2)),
                                 "{mean} ({std})".format(mean = round(aps_summary.loc[(aps_summary.condition == 4)  ,'PERC_CORRECT'].mean(),2), std = round(aps_summary.loc[(aps_summary.condition == 4)  ,'PERC_CORRECT'].std(),2)) ])


    print(myTable)
    
    
produce_table1()
produce_table1(1)
produce_table1(2)
produce_table1(3)
produce_table1(4)


##plotting what is in the table

def extract_data(block=0):
    if block == 0:
        control_final = all_correct_final[all_correct_final.group == 'control']
        control_summary = summary_dfs[summary_dfs.group == 'control']
        aps_final = all_correct_final[all_correct_final.group == 'aps']
        aps_summary = summary_dfs[summary_dfs.group == 'aps']
    else:
        control_final = all_correct_final[(all_correct_final.block == block) & (all_correct_final.group == 'control')]
        control_summary = summary_dfs[(summary_dfs.block == block) & (summary_dfs.group == 'control')]
        aps_final = all_correct_final[(all_correct_final.block == block) & (all_correct_final.group == 'aps')]
        aps_summary = summary_dfs[(summary_dfs.block == block) & (summary_dfs.group == 'aps')]

    conditions = ['SRC Plausible', 'SRC Implausible', 'ORC Plausible', 'ORC Implausible']
    data = {'Group': [], 'Condition': [], 'Mean_RT': [], 'Std_RT': [], 'Mean_AC': [], 'Std_AC': []}
    
    for group_name, final, summary in [('Control', control_final, control_summary),
                                       ('APS Native', aps_final[aps_final.speech_condition == 'french'], aps_summary[aps_summary.speech_condition == 'french']),
                                       ('APS Non-Native', aps_final[aps_final.speech_condition == 'chinese'], aps_summary[aps_summary.speech_condition == 'chinese'])]:
        for cond in range(1, 5):
            condition = conditions[cond - 1]
            data['Group'].append(group_name)
            data['Condition'].append(condition)
            data['Mean_RT'].append(final[final.condition == cond]['SENTENCE_RT'].mean())
            data['Std_RT'].append(final[final.condition == cond]['SENTENCE_RT'].std())
            data['Mean_AC'].append(summary[summary.condition == cond]['PERC_CORRECT'].mean())
            data['Std_AC'].append(summary[summary.condition == cond]['PERC_CORRECT'].std())
    
    return pd.DataFrame(data)

# Extract data for block 0 (or any other block as needed)
data = extract_data(0)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(14, 6), sharey=False)

conditions = ['SRC Plausible', 'SRC Implausible', 'ORC Plausible', 'ORC Implausible']
x = np.arange(len(conditions))  # the label locations
width = 0.2  # the width of the bars

# Plot Reaction Times (RT)
for i, group in enumerate(data['Group'].unique()):
    group_data = data[data['Group'] == group]
    positions = x + (i - 1) * width  # Offset the positions for each group
    ax[0].errorbar(positions, group_data['Mean_RT'], yerr=group_data['Std_RT'], fmt='o', label=group)

ax[0].set_title('Reaction Times (RT)')
ax[0].set_xlabel('Condition')
ax[0].set_ylabel('Mean RT')
ax[0].set_xticks(x)
ax[0].set_xticklabels(conditions)
ax[0].legend()

# Plot Accuracy (AC)
for i, group in enumerate(data['Group'].unique()):
    group_data = data[data['Group'] == group]
    positions = x + (i - 1) * width  # Offset the positions for each group
    ax[1].errorbar(positions, group_data['Mean_AC'], yerr=group_data['Std_AC'], fmt='o', label=group)

ax[1].set_title('Accuracy (AC)')
ax[1].set_xlabel('Condition')
ax[1].set_ylabel('Mean AC')
ax[1].set_xticks(x)
ax[1].set_xticklabels(conditions)
ax[1].legend()

plt.tight_layout()
plt.show()
    
