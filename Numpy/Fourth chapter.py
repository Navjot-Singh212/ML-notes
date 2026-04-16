"""Chapter number 4-- RESHAPING AND MANIPULATING ARRAYS"""
#unlike lists, arrays have a fixed size so to add new data and do other operations we need to create a new array

import numpy as np

"""np.insert(array,index num, value, axis=None)-> it is used to insert an ekement in an array

array- og array
index-
value-
axis-
if we set axis=0 the element is being inserted row wise (by default its row wise)
if axis =1 the element is being inserted column wise
"""

# arr=np.array([10,20,30,40,50])
# print(arr)

# new_arr=np.insert(arr,2,100)
# print(new_arr)

# rndmarr=np.insert(arr,2,4000)
# print(rndmarr)


"insert in 2d array"

# arr_2d= np.array([[1,2],[3,4]])
# print(arr_2d,end="\n\n")


# new_arr=np.insert(arr_2d,1,[5,6],axis=0)
# print(new_arr,end="\n\n")

# new_arr_2=np.insert(arr_2d,1,[5,6],axis=1)
# print(new_arr_2,end="\n\n")

# new_arr_3=np.insert(arr_2d,1,[5,6],axis=None)
# print(new_arr_3)


"append-> to add an element at the end of the array"
# arr=np.array([1,2,3,4,5])
# new_arr=np.append(arr,[6,7,8,9,0])
# print(new_arr)

"concatanation-> to add two arrays together"
"""
np.concatenate((arr1,arr2),axis=0)    yes there is another parenthesis for the array names

axis=0 -> adding it row wise called 'vertical stacking'
axis=1 -> adding it column wise called 'horizontal stacking'
"""
# arr1= np.array([1,2,3])
# arr2= np.array([4,5,6])
# new_arr= np.concatenate((arr1,arr2))
# print(new_arr)

#this will give error since the arrays we are adding are of the single dimension
# new_arr2=np.concatenate((arr1,arr2),axis=1)
# print(new_arr2)

# new_arr3=np.concatenate((arr1,arr2),axis=0)
# print(new_arr3) # this will give you the same output as default

"""np.delete(array,index, axis = None) -> deletes an element at a specified index

axis =None mtlb humara flattened array
 """
# arr=np.array([1,2,3,4,5])
# print(arr)
# new_arr=np.delete(arr,3)
# print(new_arr)

"for 2d deletion"
# arr=np.array([[1,2,3],[4,5,6]])
# new_arr=np.delete(arr,0,axis=0) # axis= 0 means row wise deletion
"NOTE: this will delete the whole first row of the array"
# print(new_arr)

# like we can remove an element in a simple python list by passing the element itself, unlike that numpy doesnt support that thing since it makes a new array to use this functions


"""STACKING-> basically combining multiple arrays together
may it be vertically or horizontally

vstack((arr1,arr2)) : row wise and also remember the double parenthesis
hstack((arr1,arr2)) : col wise
"""
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])

# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1,arr2)))


"""splitting-> basically splitting a single array into multiple arrays
numpy actually provides us three different functions to do so

np.split(array,number of childern arrays you want it in) : equal splitting

np.hsplit()
np.vsplit() : works only on arrays with 2 dimensions or more
"""
# arr=np.array([10,20,30,40,50,60])

# print(np.split(arr,2))

# print(np.split(arr,5))    this will result in value error since you cnat possibly split this array into 5 equal parts same error will happen if you pass numbers like 20,30 etc
# print(np.hsplit(arr,6))

# arr2d=np.array([[1,2,3],[4,5,6]])
# print(np.vsplit(arr2d,2))

"thats all the code for this chapter"