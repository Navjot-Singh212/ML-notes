"DESCRIBE METHOD -> this method provides a summary of descriptive statistics of numerous columns in the Dataframe"

import pandas as pd
data={
    "Name":["Preeti","Angad","Himanshu","aditi","priya","rohit","neha"],
    "Age":[10,20,30,25,35,40,45],
    "salary":[10000,20000,30000,25000,35000,40000,45000],
    "Performace score":[89,89,45,78,90,95,88]
}

df=pd.DataFrame(data)
print("sample data frame:")
print(df)
# print("descriptive statistics of the data frame:")
# print(df.describe())
"""
here count-> number of non null values in each column
mean-> average of the values in each column
std-> standard deviation of the values in each column   
min-> minimum value in each column
if the data is sorted then,
25%-> 25th percentile of the values in each column(0-25%) meaning that 25% of the values in each column are equal to or below this value and 75% are above this value.
50%-> 50th percentile of the values in each column(0-50%) also known as median
75%-> 75th percentile of the values in each column(0-75%) meaning that 75% of the values in each column are equal to or below this value and 25% are above this value.
max-> maximum value in each column
"""



"Shape attribute -> this attribute provides the number of rows and columns in the Dataframe"
"Columns attribute -> this attribute provides the names of the columns in the Dataframe"
# print(f"the number of rows and columns in the data frame are {df.shape}")
# print(f"the names of the columns in the data frame are {df.columns}")



"To select a specific column in the Dataframe we can use the column name as an index for example df['column name']"
print("\n\n",df['Name'])

"To select multiple columns in the Dataframe we can use a list of column names as an index for example df[['column name1','column name2']]"
print("\n\n",df[['Name','Age']])

"To filter rows based on a condition we can use boolean indexing for example df[df['column name']>value]"
print("\n\n",df[df['salary']>30000])

"To filter rows based on multiple conditions we can use the & operator for AND and | operator for OR for example df[(df['column name1']>value1) & (df['column name2']<value2)]"
# print("\n\n",df[(df['salary']>30000)& (df["salary"]<=45000)])
print("\n\n",df[(df['Age']>20) & (df["salary"]>25000)])


"thats all the code for this chapter and for Part 1 as well~"