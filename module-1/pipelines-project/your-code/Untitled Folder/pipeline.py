# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:33:39 2019
This document is about Data Cleaning and pipeline

@version: 0.1
@author: leila


"""
from __future__ import barry_as_FLUFL

# Import library
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title and input to obtain the '.png'
year= int(input('Enter year between 2000 and 2016: '))
title='Shark attack '+str(year)

def acquisition():
    df=pd.read_csv(r'D:\IRONHACK\shark\shark.csv', encoding='latin1')
    return df

def wrangling(df1):
    df1[['Year','Activity','Country','Injury' ,'Fatal (Y/N)']]

    df1=df1.rename(columns={'Fatal (Y/N)':'Fatal'})
    df1.columns
    
    #Standardisation of the columns 
    df1['Country'] = df1['Country'].str.replace(r'\W|[0-9]', ' ')
    df1['Injury'] = df1['Injury'].str.replace(r'\W|[0-9]', ' ')
    df1['Fatal'] = df1['Fatal'].str.replace(r'\W|[0-9]', ' ')
    df1['Activity'] = df1['Activity'].str.replace(r'\W|[0-9]', ' ')
    df1['Activity'] = df1['Activity'].str.strip().str.upper()
    df1['Country'] = df1['Country'].str.strip().str.upper()
    df1['Injury'] = df1['Injury'].str.strip().str.upper()
    df1['Fatal'] = df1['Fatal'].str.strip().str.upper()
    
    #Select the good words for teh cols Injury and Activity
    #Like this I will have all the activities for the col Activity
    #and for Injury I will compare if all the Fatal words = the Y Fatal in the col Fatal
    df1['Injury']=[re.findall(r'FATAL',str(x)) for x in df1['Injury']]
    df1['Activity']=[re.findall(r'\w*ING',str(x)) for x in df1['Activity']]
    
    #Fill the NaN 
    df1['Activity'].fillna("NOFILLING", inplace = True)
    df1['Country'].fillna("NO INFO", inplace = True)
    df1['Fatal']= df1['Fatal'].fillna(df1['Fatal'].mode()[0])
    df1['Country']= df1['Country'].fillna(df1['Country'].mode()[0])
    

    #Vérification des outliers et cxl
    df1.boxplot(column='Year')
    
    #Observation supplémentaire
    stats=df1.describe().T
    #Ajout de la colonne IQR (Interquartile range)
    stats['IQR']= stats['75%']- stats['25%']    
    outliers = pd.DataFrame(columns=df1.columns)
    
#    for columns in stats.index: 
#        iqr=stats.at[col,'IQR']
#        cutoff=iqr*1.6
#        lower= stats.at[col,'25%']-cutoff
#        higher= stats.at[col,'75%']+cutoff
#        results=df1[(df1[col]<lower)|(df1[col]>higher)].copy()
#        results['Outlier']=col
#        outliers=outliers.append(results)
    df1.drop(outliers.index)
    filtered = df1[df1.Year == year].copy()
    return filtered 

def analyze(filtered):
        l=[]
        for i in result.Activity:
            if len(i)>0:
                l.append(i[0])
            else:
                l.append(np.nan)
        result.Activity=l
    result = filetered.groupby('Year', as_index=False).head(10)
    return result

def viz(df):
   fig, ax= plt.subplots(figsize=(15,8))
   barchart=sns.barplot(data=df1, x='Year', y='Country')
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
    
    