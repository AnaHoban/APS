# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:38:42 2024

@author: anahoban

This code aims to perform a Wilcoxon signed-rank test on the ONLINE attractivness survey data 

"""
import scipy
import scipy.stats as stat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#create question dictionnary 
questions= {1: 'compréhensibilité',
            2: 'accent',
            3: 'intelligence',
            4: 'fiabilité',
            5: 'agréabilité',
            6: 'confiance (en soi)',
            7: 'sincérité',
            8: 'consciencieuse',
            9: 'honnêteté',
            10: 'prestige',
            11: 'éducation',
            12: 'est de confiance',
            13: 'amabilité',
            14: 'vitesse'
                }
                
question_keys = ["Comprehensibity of the native English speaker?-value",
"Comprehensibity of the non-native English speaker?-value",
"Accent of the native English speaker?-value",
"Accent of the non-native English speaker?-value",
"Intelligence of the native English speaker?-value",
"Intelligent of the non-native English speaker?-value",
"Reliability of the native English speaker?-value",
"Reliability of the non-native English speaker?-value",
"Pleasantness of the native English speaker?-value",
"Pleasantness of the non-native English speaker?-value",
"Confidence of the native English speaker?-value",
"Confidence of the non-native English speaker?-value",
"How sincere is the native English speaker?-value",
"How sincere is the non-native English speaker?-value",
"How conscientious is the native English speaker?-value",
"How conscientious is the English non-native speaker?-value",
"How honest is the native English speaker?-value",
"How honest is the non-native English speaker?-value",
"How prestigious is the native English speaker?-value",
"How prestigious is the non-native English speaker?-value",
"How educated is the native English speaker?-value",
"How educated is the non-native English speaker?-value",
"How dependable is the native English speaker?-value",
"How dependable is the non-native English speaker?-value",
"How likeable is the native English speaker?-value",
"How likeable is the non-native English speaker?-value",
"How fast does the native English speaker read?-value",
"How fast does the non-native English speaker read?-value"]

keys_dic = {  i+1: str(key)  for i, key in enumerate(question_keys)}

keys


#import data
raw_data = pd.read_csv("C:/Users/anaho/Desktop/Data_online_eng_aps/attractiveness_data_raw.csv", index_col = None, usecols = ['Participant Public ID','Object Name','Key','Response'])

#remove the duplicated participant
# Filter this participant whose data is there twice
#participant_id = '66742694149dddca1efb5cd8'
#from index = 4353 to the end
raw_data_cleaned = raw_data[raw_data['Participant Public ID'] != '66742694149dddca1efb5cd8']

# keep only rows with questions we want
useful_rows = raw_data_cleaned[raw_data_cleaned.Key.isin(question_keys)]



# pivot the dataframe
pivoted_data = useful_rows.pivot(index='Participant Public ID', columns='Key', values='Response')

pivoted_data = pivoted_data[question_keys] #reoder

# Restablecer el índice si deseas que 'Participant' vuelva a ser una columna normal
pivoted_data = pivoted_data.reset_index()


native_ans = pivoted_data.iloc[:, 1::2].astype("Int64").transpose() #type of int that accepts NA values
non_native_ans = pivoted_data.iloc[:, 2::2].astype("Int64").transpose()


#to stock values

native_means = []
non_native_means = []
p_values = []
significative = []


#perform the test
for i in range(14):
    #check if all elements are the same
    if list(native_ans.iloc[i]) == list(non_native_ans.iloc[i]):
        print('Question ', i+1, questions[i+1], 'all same')
       
        # store values 
        native_means.append(native_ans.iloc[i].mean())
        non_native_means.append(non_native_ans.iloc[i].mean())
        p_values.append(np.nan)
        significative.append(False)
        
    else:
        test_results = stat.wilcoxon(x = native_ans.iloc[i].dropna(), y = non_native_ans.iloc[i].dropna())
        
        p_value = test_results.pvalue
        
        native_mean = native_ans.iloc[i].mean()
        non_native_mean = non_native_ans.iloc[i].mean()
        
        native_means.append(native_mean)
        non_native_means.append(non_native_mean)
        p_values.append(p_value)
        significative.append(p_value < 0.05)

        
        if test_results.pvalue.round(2) < 0.05:
            print('Question ', i+1, questions[i+1], test_results.pvalue.round(10), 'SIGNIFICATIVE')
        elif test_results.pvalue.round(2) >= 0.05:
            print('Question ', i+1, questions[i+1], test_results.pvalue.round(5))
            
        print('english avg:' , native_ans.iloc[i].mean().round(2))
        print('chinese avg:', non_native_ans.iloc[i].mean().round(2))
        



# Plot
labels = [questions[i+1] for i in range(len(questions))]
x = np.arange(len(labels))  # labels
width = 0.35  # width of bars


fig, ax = plt.subplots(figsize=(4, 5))

bars1 = ax.bar(x - width/2, native_means, width, label='Native', color = 'lightblue')
bars2 = ax.bar(x + width/2, non_native_means, width, label='Non native', color = 'purple')

# Add significance * sign
for i in range(len(labels)):
    if significative[i]:
      
        #asterix
        #ax.text(x[i], max(native_means[i], non_native_means[i]) + 0.5, '*', ha='center', color='red', fontsize=14)

        # black brackets
        y = max(native_means[i], non_native_means[i]) * 1.06  # Altura de la línea
        ax.plot([x[i] - width, x[i] + width], [y, y], color='black', linewidth=1)  # Línea horizontal
        ax.plot([x[i] - width, x[i] - width], [y, y - 0.1], color='black', linewidth=1)  # Extremo izquierdo
        ax.plot([x[i] + width, x[i] + width], [y, y - 0.1], color='black', linewidth=1)  # Extremo derecho
        # Asterisco
        ax.text(x[i], y * 1.01, '*', ha='center', color='red', fontsize=14)

# Formatting
ax.set_ylim(0, max(max(native_means), max(non_native_means)) * 1.15) #adjust height
ax.set_xlabel('Attribute')
ax.set_ylabel('Average score')
ax.set_title('Online English Attractiveness Survey Results (n=84 participants)')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.legend(fontsize = 10)

plt.tight_layout()
plt.show()        

plt.savefig("C:/Users/anaho/Desktop/research/Language/APS/analysis/plots/online_english")
        
