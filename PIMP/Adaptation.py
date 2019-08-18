# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:27:38 2019

@author: Administrator
"""

import pandas as pd
import numpy

Pfile = pd.read_csv('C:/Users/Administrator/Documents/Tweet/P0.csv')
Pred = pd.read_csv('C:/Users/Administrator/Documents/Tweet/pred.csv')

Means = []
for i in range (1,11):
    Means.append(Pred[Pred['SpeakerID'] == i]['Depressed'].values.mean())

print(Means)
    
PfileClone = Pfile.copy()
PfileClone['CaseBased'] = -1

for SampleID2 in PfileClone['ID2'].values:
    Speaker = Pred[Pred ['ID']==SampleID2]['SpeakerID']
    
    if(Speaker.values[0] <= 5):
        ScoreofID2 = Pred[Pred ['ID']==SampleID2]['Depressed'].values[0]
        SampleID1 = PfileClone[PfileClone['ID2'] == SampleID2]['ID1'].values[0]
        ScoreofID1 = Pred[Pred ['ID']==SampleID1]['Depressed'].values[0]
        print(Speaker.values[0])
        if (Speaker.values[0] == 5 and ScoreofID1 < ScoreofID2):
            print('= 5')
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = 5
        elif(Speaker.values[0] == 1 and ScoreofID1 > ScoreofID2):
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = 1
            print('= 1')
        else:
            print('find min')
            index = (numpy.abs(Means[0:5]-ScoreofID1)).argmin()
            print(index)
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = index+1
            
    elif(Speaker.values[0] <= 10):
        
        ScoreofID2 = Pred[Pred ['ID']==SampleID2]['Depressed'].values[0]
        SampleID1 = PfileClone[PfileClone['ID2'] == SampleID2]['ID1'].values[0]
        ScoreofID1 = Pred[Pred ['ID']==SampleID1]['Depressed'].values[0]
        print(Speaker.values[0])
         
        if (Speaker.values[0] == 10 and ScoreofID1 < ScoreofID2):
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = 10
            print('= 10')
        elif(Speaker.values[0] == 6 and ScoreofID1 > ScoreofID2):
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = 6
            print('= 6')
        else:
            print('find min2')
            index = (numpy.abs(Means[5:10]-ScoreofID1)).argmin()
            print(index)
            PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = index+6
    else:
        PfileClone.loc[PfileClone['ID2'] == SampleID2,'CaseBased'] = 11

PfileClone.to_excel('Result.xlsx')