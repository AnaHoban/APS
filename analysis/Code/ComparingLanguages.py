import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable 
import numpy as np

# Eyetracking data
control_final_french = pd.read_csv('../data/CORR_clean_french_online_silentData_formatted.csv', encoding='latin1')
control_summary_french = pd.read_csv('../data/CORR_summary_clean_french_online_silentData_formatted.csv', encoding='latin1')

control_final_french['language'] = 'french'
control_summary_french['language'] = 'french'

control_final_english = pd.read_csv('../data/CORR_clean_only_control_data.csv', encoding='latin1')
control_summary_english = pd.read_csv('../data/CORR_summary_clean_only_control_data.csv', encoding='latin1')

control_final_english['language'] = 'english'
control_summary_english['language'] = 'english'

print(control_final_english.head(3))


# Combining all final and summary data
all_final = pd.concat([control_final_french, control_final_english], ignore_index=True)
summary_dfs = pd.concat([control_summary_french, control_summary_english], ignore_index=True)

def get_means2(df, y_to_plot, group):
    mean_cond1 = df.loc[(df.condition == 1) & (df.language == group), y_to_plot].mean()
    mean_cond2 = df.loc[(df.condition == 2) & (df.language == group), y_to_plot].mean()
    mean_cond3 = df.loc[(df.condition == 3) & (df.language == group), y_to_plot].mean()
    mean_cond4 = df.loc[(df.condition == 4) & (df.language == group), y_to_plot].mean()
    return mean_cond1, mean_cond2, mean_cond3, mean_cond4

def plot_means2(means, group):
    if group == 'french':
        mins = [0.05, 0.3, 0.55, 0.8] 
        maxs = [0.12, 0.36, 0.62, 0.86]
    elif group == 'english':
        mins = [0.14, 0.40, 0.64, 0.90]
        maxs = [0.22, 0.46, 0.70, 0.96]
     
    for i, mean in enumerate(means):
        ax.axhline(mean, xmin=mins[i], xmax=maxs[i], ls='--', color='r')
    return means

labels = ['subject plausible', 'subject implausible', 'object plausible', 'object implausible']
data = all_final
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x='condition', y='SENTENCE_RT', hue="language", data=data, saturation=0.5, boxprops={'alpha': 0.4})
sns.stripplot(x='condition', y='SENTENCE_RT', hue='language', data=data, dodge=True, ax=ax, alpha=0.5)
plot_means2(get_means2(data, 'SENTENCE_RT', 'french'), 'french')
plot_means2(get_means2(data, 'SENTENCE_RT', 'english'), 'english')
fig.set_xticklabels(labels)
fig.set_ylabel('Reading time (log and norm)')
fig.set_title('RTs For All answers')
plt.savefig('../plots/reading_times_online')

data = summary_dfs
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x='condition', y='PERC_CORRECT', data=data, hue='language', boxprops={'alpha': 0.8})
fig.set_xticklabels(labels)
plot_means2(get_means2(data, 'PERC_CORRECT', 'french'), 'french')
plot_means2(get_means2(data, 'PERC_CORRECT', 'english'), 'english')
fig.set_ylabel('Proportion of correct answers')
fig.set_title('Paraphrase Accuracy')
plt.savefig('../plots/corr_answers_online.png')

def produce_table1(block=0):
    myTable = PrettyTable(["Language", "Structure", "RT - Plausible", "RT - Implausible", "AC - Plausible", "AC - Implausible"])

    if block == 0:
        control_final = all_final
        control_summary = summary_dfs
    else:
        control_final = all_final[all_final.block == block]
        control_summary = summary_dfs[summary_dfs.block == block]
    
    languages = ['french', 'english']

    for lang in languages:
        # Add rows for each language
        myTable.add_row([lang.capitalize(), "SRC", 
                         "{mean} ({std})".format(mean=round(control_final.loc[(control_final.condition == 1) & (control_final.language == lang), 'SENTENCE_RT'].mean()), 
                                                  std=round(control_final.loc[(control_final.condition == 1) & (control_final.language == lang), 'SENTENCE_RT'].std())),
                         "{mean} ({std})".format(mean=round(control_final.loc[(control_final.condition == 2) & (control_final.language == lang), 'SENTENCE_RT'].mean()), 
                                                  std=round(control_final.loc[(control_final.condition == 2) & (control_final.language == lang), 'SENTENCE_RT'].std())),
                         "{mean} ({std})".format(mean=round(control_summary.loc[(control_summary.condition == 1) & (control_summary.language == lang), 'PERC_CORRECT'].mean(), 2), 
                                                  std=round(control_summary.loc[(control_summary.condition == 1) & (control_summary.language == lang), 'PERC_CORRECT'].std(), 2)),
                         "{mean} ({std})".format(mean=round(control_summary.loc[(control_summary.condition == 2) & (control_summary.language == lang), 'PERC_CORRECT'].mean(), 2), 
                                                  std=round(control_summary.loc[(control_summary.condition == 2) & (control_summary.language == lang), 'PERC_CORRECT'].std(), 2))])
        myTable.add_row([" ", "ORC", 
                         "{mean} ({std})".format(mean=round(control_final.loc[(control_final.condition == 3) & (control_final.language == lang), 'SENTENCE_RT'].mean()), 
                                                  std=round(control_final.loc[(control_final.condition == 3) & (control_final.language == lang), 'SENTENCE_RT'].std())),
                         "{mean} ({std})".format(mean=round(control_final.loc[(control_final.condition == 4) & (control_final.language == lang), 'SENTENCE_RT'].mean()), 
                                                  std=round(control_final.loc[(control_final.condition == 4) & (control_final.language == lang), 'SENTENCE_RT'].std())),
                         "{mean} ({std})".format(mean=round(control_summary.loc[(control_summary.condition == 3) & (control_summary.language == lang), 'PERC_CORRECT'].mean(), 2), 
                                                  std=round(control_summary.loc[(control_summary.condition == 3) & (control_summary.language == lang), 'PERC_CORRECT'].std(), 2)),
                         "{mean} ({std})".format(mean=round(control_summary.loc[(control_summary.condition == 4) & (control_summary.language == lang), 'PERC_CORRECT'].mean(), 2), 
                                                  std=round(control_summary.loc[(control_summary.condition == 4) & (control_summary.language == lang), 'PERC_CORRECT'].std(), 2))])
        myTable.add_row([" " , " " , " " , " " , " " , " "])

    print(myTable)

produce_table1()
produce_table1(1)
produce_table1(2)
produce_table1(3)
produce_table1(4)

# Plotting what is in the table
def extract_data(block=0):
    if block == 0:
        control_final = all_final
        control_summary = summary_dfs
    else:
        control_final = all_final[all_final.block == block]
        control_summary = summary_dfs[summary_dfs.block == block]

    conditions = ['SRC Plausible', 'SRC Implausible', 'ORC Plausible', 'ORC Implausible']
    data = {'Language': [], 'Condition': [], 'Mean_RT': [], 'Std_RT': [], 'Mean_AC': [], 'Std_AC': []}
    
    for lang in ['french', 'english']:
        for cond in range(1, 5):
            condition = conditions[cond - 1]
            data['Language'].append(lang)
            data['Condition'].append(condition)
            data['Mean_RT'].append(control_final[(control_final.condition == cond) & (control_final.language == lang)]['SENTENCE_RT'].mean())
            data['Std_RT'].append(control_final[(control_final.condition == cond) & (control_final.language == lang)]['SENTENCE_RT'].std())
            data['Mean_AC'].append(control_summary[(control_summary.condition == cond) & (control_summary.language == lang)]['PERC_CORRECT'].mean())
            data['Std_AC'].append(control_summary[(control_summary.condition == cond) & (control_summary.language == lang)]['PERC_CORRECT'].std())
    
    return pd.DataFrame(data)

data = extract_data(0)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

sns.barplot(x='Condition', y='Mean_RT', hue='language', data=data, ax=ax[0])
ax[0].set_title('Mean RTs by Condition and Language')
ax[0].set_ylabel('Reading time (log and norm)')

sns.barplot(x='Condition', y='Mean_AC', hue='language', data=data, ax=ax[1])
ax[1].set_title('Mean Accuracy by Condition and Language')
ax[1].set_ylabel('Proportion of correct answers')

plt.show()
