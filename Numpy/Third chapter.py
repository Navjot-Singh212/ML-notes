"""chapter 3- INDEXING AND SLICING"""
import numpy as np

"""
array[index]  # for 1D array
array[row_index, column_index]  # for 2D array"""
# arr=np.array([10,20,30,40,50])

# print(arr[0])  # 10
# print(arr[2])  # 30
# print(arr[-1]) # 50 last element

"slicing is used to access a range of elements in an array"
"array[start:stop:step] where stop is exclusive meaning it will go like start to end-1 "
# print(arr[1:4])  # [20 30 40]
# print(arr[:3])   # [10 20 30] start is by default 0
# print(arr[2:])   # [30 40 50] stop is by default the end of the array

# #negative step -1 will reverse the array
# print(arr[::-1])  # [50 40 30 20 10]

# print(arr[::2])  # [10 30 50] every second element


"""fancy indexing is used to access multiple elements at once"""
# arr=np.array([10,20,30,40,50])    

#when we use fancy indexing the result we see is a copy of the elements and not the original elements itself
# that means no need to worry about the original data being modified


"""boolean masking is basically filtering data on conditions"""
# print(arr[arr>25])  # [30 40 50] access elements greater than 25


"RESHAPING AND MANIPULATING ARRAYS "
#Reshaping an array means changing its shape without changing its data

"arr.reshape(rows, columns) also you can only reshape if the dimensions match"
# rndmarr=np.array([1,2,3,4,5,6])
# reshaped_arr=rndmarr.reshape(2,3)  # reshape to 2 rows and 3 columns
# print(reshaped_arr)
#reshaping does not create of copy but returns a view
#so changes to reshaped_arr will affect arr and vice versa
#new array humare og array ko affect krega

"flattening an array"
"""
ravel()
and
flatten()

'used to convert multi dimensional array into 1D array'
"""

# .ravel()--> views -- returns a view of the original array meaning modifcation to the og array will happen
# .flatten()-->copy-- returns the copy of the original array meaning modification to the og array will not happen
# arr_2d=np.array([[1,2,3],[4,5,6]])
# print(arr_2d.ravel())
# print(arr_2d.flatten())

"this is all the code for this chapter"