"HANDLING MISSING DATA "

"""
NaN(not a number)
None(for object data type)
these are the two types of missing data in pandas
"""
import pandas as pd

"""isnull() method-> this method is used to check for missing values in the Dataframe(remember that it will return True and False in the form of the original dataframe),
if it returns True then the value is  missing 
and if it returns False then the value is not missing
"""

data={
    "Name":["Preeti",None,"Himanshu","aditi","priya","rohit","neha"],
    "Age":[10,None,30,25,35,40,45],
    "salary":[10000,None,30000,25000,35000,40000,45000],
    "Performance score":[89,None,45,78,90,95,88]
}
df=pd.DataFrame(data)
# print("sample missing value data frame:")
# print(df)
# print(f"\n{df.isnull()}")
# print(df.isnull().sum())  # this will give you the series of count of missing values in each column


"""
df.dropna(axis=0 or 1, inplace=True) -> this method is used to drop the rows and columns with missing values from the Dataframe
here if axis=0 then it drops the rows(yes the whole row) with missing values
and if axis=1 then it drops the columns with the missing values
"""
# df.dropna(axis=0,inplace=True) # btw axis is 0 by default
# print(df) 

"""
fillna() method-> this method is used to fill the missing values in the Dataframe with a specific value"""

df.fillna(0,inplace=True)
# print("\n\n",df)

# df["Age"].fillna(df["Age"].mean(),inplace=True)
# df["salary"].fillna(df["salary"].mean(),inplace=True)
# these two way of writing will not work well in the future with the next Pandas update so use reassignment


#since in the prev step we changed the nan values to zero we need to change them back to nan to be detected as nan for the next step
df["Age"]=df["Age"].replace(0,None)
df["salary"]=df["salary"].replace(0,None)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["salary"]=df["salary"].fillna(df["salary"].mean())
# print("\n\n",df)


"""
df.interpolate(method='linear',axis=0,inplace=True) :Interpolation method-> this method is used to fill the missing values in the Dataframe with the help of interpolation technique
Interpolation technique is a technique used to fill the missing values with estimmated values based on the existing values in the Dataframe

method is the algorithm used for interpolation,
some of the methods are:
linear, polynomial, time etc, similarly there are many other methods for interpolation
"""

data2={
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}
df2=pd.DataFrame(data2)
print("before interpolation...")
print(df2)

print("after linear interpolation...")
df2['value']=df2['value'].interpolate(method="linear",axis=0)
print(df2)

print("after polynomial interpolation...")
df2['value']=df2["value"].interpolate(method='polynomial',order=2,axis=0)
print(df2)

"""
when to use interpolation:
when dealing with time series data,
numberic data with a clear trend or pattern,
avoid dropping rows or columns with missing values.
"""

"thats all the code for this chapter..."