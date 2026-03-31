"SORTING AND AGGREGATION(summary stats)"

import pandas as pd

"sorting dataframe:"

#sorting data in a single column
"df.sort_values(by='column name',ascending=True or False,inplace= True or False)"

data={
    "name":["talat","neel","rose","prachi","Hajna"],
    "age":[20,22,34,34,19],
    "salary":[10000,30000,20000,4000,5500]
}
df=pd.DataFrame(data)
print("sample dataframe:")
# print(df)
# df.sort_values(by="age",ascending=True,inplace=True)
# print("sorted age by ascending...")
# print(df)

#sorting multiple columns
#for that we need to past a list both in by and ascending parameters
df.sort_values(by=["age","salary"],ascending=[True,True],inplace=True)
print(df)
#remember that sort_values() method has a preference order meaning the column passed first in the by parameter will be the primary sorting rule





"AGGREGATION~"
print("the mean of the salary is:",df["salary"].mean())
print("the total sum of the salary is:",df["salary"].sum())
print("the minimum salary is:",df["salary"].min())
print("the maximum salary an employee here has is:",df["salary"].max())
print("the number of non-nan values in the salary is:",df["salary"].count())
print(f"the standard deviation of the salary is:{df["salary"].std():.3f}")

"""
df.groupby('column name you want to group acc to')[column you want to perfrom aggregation operation on].sum/operation
the column name you pass in the () is the column according to whose unique values you want to group by it.
"""
grouped=df.groupby('age')["salary"].sum()
print(grouped)

#grouping by multiple columns
groupedmul=df.groupby(["age","name"])["salary"].sum()
print(groupedmul)


"thats all the code for this chapter..."