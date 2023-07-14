# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:58:59 2023

@author: EZRA
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#2 methods to import a json file
#method 1

json_file= open('C:/Users/EZRA/Downloads/Python and Tableau Course/loan_data_json.json')
dataset=json.load(json_file)

#medhod 2

with open('C:/Users/EZRA/Downloads/Python and Tableau Course/loan_data_json.json') as jsonfile2:
        dataset2=json.load(jsonfile2)
   
        

#Transforming json file to datafram using pandas
    
LoanDataset = pd.DataFrame(dataset)




#using describe function

LoanDataset["purpose"].describe()

LoanDataset.describe()




#using unique()

LoanDataset['purpose'].unique()



#working with array

#1D array
arr= np.array([1,2,3,4])

arr2=np.array(43)

#2D array
arr3 = np.array([[1,2,3],[4,5,6]])


#using exp()

#assigning variable income

income=np.exp(LoanDataset['log.annual.inc'])
LoanDataset['AnnualIncome']= income


LoanDataset.info()

#using if,elif,else to create category for fico column



fico = 700

if fico >= 300 and fico < 400:
    FicoCategory = 'Very Poor'
elif fico >= 400 and fico < 600:
    FicoCategory = 'Poor'
elif fico >= 601 and fico < 660:
    FicoCategory = 'Fair'
elif fico >= 660 and fico < 780:
    FicoCategory = 'Good'
elif fico >= 827:
    FicoCategory= 'Excellent'
else:
    FicoCategory='Unknown'

print(FicoCategory)    


LoanDataset["fico"].describe()



#applying for loop to the dataset

length = len(LoanDataset)
category=[]

for x in range(length):
    fico = LoanDataset['fico'][x]
    if fico >= 300 and fico < 400:
        FicoCategory = 'Very Poor'
    elif fico >= 400 and fico < 600:
        FicoCategory = 'Poor'
    elif fico >= 601 and fico < 660:
        FicoCategory = 'Fair'
    elif fico >= 660 and fico <= 780:
        FicoCategory = 'Good'
    elif fico >= 781 and fico <= 827:
        FicoCategory= 'Excellent'
    else:
        FicoCategory='Unknown'
    category.append(FicoCategory)
        


        

LoanDataset["FicoCategory"] = category = pd.Series(category)     


#using df.loc

LoanDataset.loc[LoanDataset["int.rate"] > 0.12,'IntRateType']= 'High'
LoanDataset.loc[LoanDataset["int.rate"] <= 0.12,'IntRateType']= 'Low'


# using group by and plotting the data 

inquery=LoanDataset.groupby(['inq.last.6mths']).size()
inquery.plot.bar(color= 'blue')
plt.show()

#creating scatterplot

xaxis = LoanDataset["dti"]
yaxis = LoanDataset["AnnualIncome"]
plt.scatter((xaxis), yaxis, color='green')
plt.show()

#LoanDataset

LoanDataset.info()

LoanDataset = LoanDataset.rename(columns = {
    'credit.policy': 'Credit_Policy',
    'purpose':'Purpose',
    'int.rate':'Int_Rate',
    'installment':'Installment',
    'log.annual.inc':'Log_Annual_Inc',
    'dti':'Dti',
    'fico':'Fico',
    'days.with.cr.line':'Days_With_Cr_Line',
    'revol.bal':'Revol_Bal',
    'revol.util':'Revol_Util',
    'inq.last.6mths':'Inq_Last_6Mths',
    'delinq.2yrs':'Delinq_2Yrs',
    'pub.rec':'Pub_Rec',
    'not.fully.paid':'Not_Fully_Paid',
    ' AnnualIncome':' Annual_Income',
    'FicoCategory':'Fico_Category',
    'IntRateType':'Int_Rate_Type'
                                  } )





#LoanDataset.to_csv('BlueBank.csv',LoanDataset['ID']==index= True)

























































































































