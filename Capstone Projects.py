""" Capstone Projects"""

# importing libraries
import numpy as np
import pandas as pd

#loading the dataset and displaying a few rows
df=pd.read_csv("sales_data_sample.csv",encoding='latin1')
print(df.head())

#checking for missing values
print(df.isna().sum())

#handling the missing values

#we have some non integer values(str) in the postal so lets first convert every cell of the postal column
df['POSTALCODE']=pd.to_numeric(df['POSTALCODE'],errors='coerce')
postal_mean=df['POSTALCODE'].mean()
df['POSTALCODE']=np.nan_to_num(df['POSTALCODE'],nan=postal_mean)

df['ADDRESSLINE2']=df['ADDRESSLINE2'].fillna("not specified")
df['STATE']=df['STATE'].fillna('not specified')
df['TERRITORY']=df['TERRITORY'].fillna('not specified')
print(df.isna().sum())

#handling the infinite values
#right now we dont have any infinite values in the data so lets inject some in it to practice on them
column_to_messup='PRICEEACH'
random_indices=df.sample(n=5,random_state=42).index
df.loc[random_indices,column_to_messup]=np.inf
print("infinites injected successfully")
print(df.isin([np.inf,-np.inf]).sum())

df['PRICEEACH']=np.nan_to_num(df['PRICEEACH'],posinf=1000,neginf=0)
print(df.isin([np.inf,-np.inf]).sum())

#we dont have negative values in the dataset so lets inject that as well
random_indices=df.sample(n=5,random_state=42).index
df.loc[random_indices,column_to_messup]=-222
print("negatives injected successfully")
print((df['PRICEEACH']<0).sum())

cleanmean=df[df['PRICEEACH']>=0]['PRICEEACH'].mean()
df['PRICEEACH']=np.where(df['PRICEEACH']<0,cleanmean,df['PRICEEACH'])
print((df['PRICEEACH']<0).sum())

#check if you want to clip the data(any outliers) i checked my data and i want to keep it as it is.
df.to_csv('cleaned_sales_data)sample.csv',index=False)
print("clean dataset saved successfully!!!!!!")