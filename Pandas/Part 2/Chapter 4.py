"MERGING AND JOINING"

import pandas as pd
"Merging refers to the process of combining rows of 2 or more data frames based on a common key name"

"""
pd.merge(df1,df2,on="Column_name",how="type of join")
where you have to pass the common column name in the on parameter and,
in how you pass how you want to join the data frames and there are 5 ways to join the data frames:
1. inner join: this will return only the common rows in both the data frames based on the common column name
2. Outer join: this will return all the rows in both the data frames and if there is no common row in one of the data frames then it will return NaN for that row
3. Left join: this will return all the rows in the left data frame and if there is no common row in the right data frame then it will return NaN for that row
4. Right join: this will return all the rows in the right data frame and if there is no common row in the left data frame then it will return NaN for that row
5. Cross join: this will return the cartesian product of the two data frames meaning it will return all the possible combinations of the rows in both the data frames
"""

df_customers=pd.DataFrame({
    "customerID":[1,2,3],
    "name":['Ramesh','Kalesh','Suresh']
})

df_orders=pd.DataFrame({
    "customerID":[1,2,4],
    "orderprice":[1000,234,456]
})

merged=pd.merge(df_customers,df_orders,on="customerID",how="inner")
# print(merged)

merged2=pd.merge(df_customers,df_orders,on="customerID",how="outer")
# print(merged2)

merged3=pd.merge(df_customers,df_orders,on="customerID",how="left")
# print(merged3)

merged4=pd.merge(df_customers,df_orders,on="customerID",how="right")
# print(merged4)

merged5=pd.merge(df_customers,df_orders,how="cross") # yes cross join does not require a common column name to join the data frames
# print(merged5)
#here in this dataframe it will make a confusing dataframe as an output but it is basically the combinaion of all the rows in both the data frames



"""Concatanation:
vertically: row wise (by default)
horizontally: column wise
pd.concat([df1,df2],axis=0 or 1,ignore_index=True or False)
where you have to pass the data frames in a list and axis is the parameter to specify whether you want to concatenate the data frames vertically or horizontally and ignore_index is the parameter to specify whether you want to reset the index of the concatenated data frame or not
"""
df_region1=pd.DataFrame({
    "customerID":[1,2],
    "region":['Mighty','Raju']
})
df_region2=pd.DataFrame({
    "customerID":[3,4],
    "region":['Suresh','Kalesh']
})
cont=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(cont)

"thats all the code for this chapter, this part and these notes as well~"