# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:44:11 2019

@author: leila
"""

#Import librairies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

year= int(input('Enterthe year: '))
title='Top 10 Car Producers by Fuel Efficiency in '+str(year)

def acquisition():
    data=pd.read_csv(r'D:\IRONHACK\vehicles\vehicles\vehicles.csv')
    return data

def wrangling(df):
    filtered = df[df.Year == year].copy()
    return filtered 

def analyze(filtered):
    result = filetered.groupby('Make', as_index=False)['Combined MPG'].mean().sort_values(by= 'Combined MPG',ascending=False).head(10).round(1)
    return result

def viz(df):
    fig, ax= plt.subplots(figsize=(15,8))
    barchart=sns.barplot(data=df, x='Make', y='Combined MPG')
    plt.title(title+'\n',fontsize=16)
    sns.set_style('darkgrid')
    plt.show()
    return barchart

def save_viz(chart):
    fig= chart.get_figure()
    fig.savefig(title+'.png')

if __name__=='__main__':
    data=acquisition()
    filetered=wrangling(data)
    results=analyze(filetered)
    barchart=viz(results)
    save_viz(barchart)
    
    