# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:16:47 2024

@author: anaho
"""

#import statements
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import math
import warnings

from prettytable import PrettyTable 

warnings.filterwarnings('ignore')

#####################################################


#functions for DataCleaning.py file

def scaling(series):
    # Convert the series to a 2D array if necessary
    series_2d = series.values.reshape(-1, 1)
    
    # Initialize the scaler
    sc = StandardScaler()
    
    # Fit the scaler to the series
    sc.fit(series_2d)
    
    # Transform the series
    scaled_series = sc.transform(series_2d)
    
    # Convert the result back to a 1D array (if necessary)
    scaled_series = scaled_series.flatten()
    
    return scaled_series


#function for DescriptiveStats.py file

def get_means(df, y_to_plot):
    mean_cond1 = df.loc[(df.condition == 1), y_to_plot].mean()
    mean_cond2 = df.loc[(df.condition == 2), y_to_plot].mean()
    mean_cond3 = df.loc[(df.condition == 3), y_to_plot].mean()
    mean_cond4 = df.loc[(df.condition == 4), y_to_plot].mean()
    
    return mean_cond1, mean_cond2, mean_cond3, mean_cond4

def plot_across_conditions(df, var):
    labels = ['subject plausible','subject implausible', 'object plausible','object implausible']
    data = pd.concat([df['condition'], df[var]], axis=1)
    f, ax = plt.subplots(figsize=(8, 6))
    fig = sns.boxplot(x='condition', y=var, data=data)
    sns.stripplot(x='condition', y=var, data=data,dodge=True, ax=ax)
    fig.set_xticklabels(labels);
    
    #plot the means
    mins = [0.05,0.3,0.55,0.8] 
    maxs = [0.2,0.45,0.7,0.95]
     
    for i,mean in enumerate(get_means(data,var)):
        ax.axhline(mean, xmin = mins[i], xmax = maxs[i], ls='--', color = 'y')
        
