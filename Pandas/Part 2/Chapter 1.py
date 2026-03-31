"Modifying data"

import pandas as pd



data={
    "Name":["Preeti","Angad","Himanshu","aditi","priya","rohit","neha"],
    "Age":[10,20,30,25,35,40,45],
    "salary":[10000,20000,30000,25000,35000,40000,45000],
    "Performance score":[89,89,45,78,90,95,88]
}
df=pd.DataFrame(data)
print("sample data frame:")
# print(df)

"df['Column name']=some data-> adding columns"
# df["bonus"]=df["salary"]*0.2
# print("\n\n",df)

# df["total salary"]=df["bonus"]+df["salary"]
# print(df)

"df.insert(loc,'column name',some data)   >adding columns using insert() method : by using this we can add a column at an index we specify "
"here loc is location or index to add the column at"
df.insert(3,"Bonus!!",df["salary"]*0.2)
print(df)



"df.loc[row_index,'column name']= new_value  -> a method used to access a specific cell or set of cells or rows or columns"
# print(df.loc[3])   # this will give you all the details/key-value pair of the index asked
# print(df.loc[3,"salary"])  # this will give you the salary of the index asked
# df.loc[3,"salary"]=60000  # this will change the salary of the index asked to the new value
# print(df.loc[3,"salary"])  # this will give you the updated salary of the index asked

"now to change multiple values at once,"
# df["salary"]*=1.5
# print(df)


"df.drop(columns=['Column Name'],inplace=True) -> this method is used to drop a column or row from the Dataframe"
"""
here columns is used to specify the column name to drop and,
inplace means that the change will be made in the original Dataframe if inplace is True and if inplace is False then a new Dataframe will be returned with the column dropped and the original Dataframe will remain unchanged.
"""

df.drop(columns=["Performance score","Age"],inplace=True)
print("modified data frame:")
print(df)