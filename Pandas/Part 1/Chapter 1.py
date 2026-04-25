"Key pandas concepts:"

"""
1. Series: A one-dimensional labeled array capable of holding any data type. It is similar to a column in a spreadsheet or a SQL table.
2.DataFrame: A two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or a SQL table. where,
- rows have indices(labels) and columns have names.

"""
import pandas as pd

df=pd.read_csv("sales_data_sample.csv",encoding="latin1")     #remember if you dont generate the data yourself which you usually won't you might need to tackle encoding.
# # basically in the bracket above just add , encoding="latin1" or "utf-8" where utf-8 and latin1 both are encoding standards. If you get an error while reading the csv file try changing the encoding to one of these two and see if it works.
# print(df)


"Similarly there are other functions to read different file formats like read_excel, read_json, read_sql, etc. depending on the format of your data."
"if you have a data stored in google cloud you can use the gcsfs library to read the data directly into a pandas dataframe using the read_csv function with the appropriate file path and credentials."


"Here's how to create a Dataframe using dictionary:"
data={
    "Name":["Preeti","Angad","Himanshu"],
    "Age":[10,20,30],
    "City":["jagadhri","yamunanagar","Dholakpur"]
}
df1=pd.DataFrame(data)
# print(df1)

".to_csv(name you want to save the file +.csv)->  to save this data in csv file "
# df1.to_csv("output.csv",index=False)    #you will see a file with the name you mentioned in the folder where this file is stored

#now if you run df1 you will see that it is printed with index starting from 0 to remove that:
#in the to_csv() method write index=False after the file name in the ()

"to_excel(file.xlsx,index=False) -> this is a similar method but instead the Dataframe is converted to an excel file "
df1.to_excel("output.xlsx",index=False)

"similarly there are methods for to_json() etc"





"""EXPLORING DATA:"""

"1. head(n): This method returns the first n rows of the DataFrame. By default, it returns the first 5 rows."
"2. tail(n): This method returns the last n rows of the DataFrame. By default, it returns the last 5 rows." 
# print("Displaying 10 rows of the start...")
# print(df.head(10))
# print("Displaying 10 rows of the end...")
# print(df.tail(10))


"info()-> this methods tells us the number of rows and columns, column names, data types of each olumn such as int64 float64 object, non null counts ,memory usage etc."
print("printing the info of the dataset...")
# print(df.info())
# print(df1.info())

"that was all the code for this chapter!!"
