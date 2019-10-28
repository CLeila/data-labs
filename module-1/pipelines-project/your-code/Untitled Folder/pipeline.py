# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:33:39 2019

@author: leila
"""

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

year= int(input('Enter year between 2000 and 2016: '))
title='Shark attack '+str(year)

def acquisition():
    df=pd.read_csv(r'D:\IRONHACK\shark\shark.csv', encoding='latin1')
    return df

df1=df[['Year','Activity','Country','Injury' ,'Fatal (Y/N)']]

df1=df1.rename(columns={'Fatal (Y/N)':'Fatal'})
df1.columns

#Observation et mise en forme des données 
df1['Country'] = df1['Country'].str.replace(r'\W|[0-9]', ' ')
df1['Injury'] = df1['Injury'].str.replace(r'\W|[0-9]', ' ')
df1['Fatal'] = df1['Fatal'].str.replace(r'\W|[0-9]', ' ')
df1['Activity'] = df1['Activity'].str.replace(r'\W|[0-9]', ' ')
df1['Activity'] = df1['Activity'].str.strip().str.upper()
df1['Country'] = df1['Country'].str.strip().str.upper()
df1['Injury'] = df1['Injury'].str.strip().str.upper()
df1['Fatal'] = df1['Fatal'].str.strip().str.upper()

df1['Activity'].fillna("NOFILLING", inplace = True)
df1['Country'].fillna("NO INFO", inplace = True)
df1['Injury']=[re.findall(r'FATAL',str(x)) for x in df1['Injury']]
df1['Activity']=[re.findall(r'\w*ING',str(x)) for x in df1['Activity']]

df1['Fatal']= df1['Fatal'].fillna(df1['Fatal'].mode()[0])
df1['Country']= df1['Country'].fillna(df1['Country'].mode()[0])

low_variance=[]
for col in df1._get_numeric_data():
    minimum= min(df1[col])
    ninety_perc =  percentile(df1[col], 90)
    if minimum == ninety_perc:
        low_variance.append(col)

#Vérification des outliers
df1.boxplot(column='Year')

#Observation supplémentaire
stats=df1.describe().T

#Ajout de la colonne IQR (Interquartile range)
stats['IQR']= stats['75%']- stats['25%']
stats

outliers = pd.DataFrame(columns=df1.columns)
outliers

for columns in stats.index: 
    iqr=stats.at[col,'IQR']
    cutoff=iqr*1.6
    lower= stats.at[col,'25%']-cutoff
    higher= stats.at[col,'75%']+cutoff
    results=df1[(df1[col]<lower)|(df1[col]>higher)].copy()
    results['Outlier']=col
    outliers=outliers.append(results)
    
outliers.head(5)
df1.drop(outliers.index)


def wrangling(df):
    filtered = df[df.Year == year].copy()
    return filtered 

def analyze(filtered):
    result = filetered.groupby('Year', as_index=False).head(10)
    return result

def viz(df):
   fig, ax= plt.subplots(figsize=(15,8))
   barchart=sns.barplot(data=result, x='Year', y='Country')
   plt.title(title+'\n',fontsize=16)
   sns.set_style('darkgrid')
   plt.show()
   return barchart

def save_viz(chart):
    fig= chart.get_figure()
    fig.savefig('.png')

if __name__=='__main__':
    data=acquisition()
    filetered=wrangling(data)
    results=analyze(filetered)
    barchart=viz(results)
    save_viz(barchart)
    
    