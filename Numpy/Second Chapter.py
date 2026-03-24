"""array properties and operations"""

import numpy as np

#how do we check the shape, size and type of an array


#for dimensions we use
""".shape"""

# arr2=np.array([[1,2,3],
#               [5,6,7]])
# print(arr2.shape)

#for total number of elements in an array
""".size"""
# print(arr2.size)

#to check number if dimensions
""".ndim"""

# arr1=np.array([1,2,3])
# arr3=np.array([[[1,2,3],[1,2,3],[2,2,3]]])
# print(arr2.ndim)
# print(arr1.ndim)
# print(arr3.ndim)

#to check the data type of the elements stored in an array
# print(arr2.dtype)



# now if we want to change the data type of the elements in an array
""".astype(newtype)"""

# strarr=arr1.astype(str)
# print(strarr)
# print(strarr.dtype)
# fltarr=arr1.astype(float)
# print(fltarr, fltarr.dtype)



"""numpy operators"""

""" operators               example"""
    # +                      arr +2 
    # -                      arr-2
    # *                      arr*3
    # /                      arr/2
    # and so on

# arrA=np.array([10,20,30,40])
# print(arrA*2)
# print(arrA+2)
# print(arrA**2)


"""AGGREGATION FUNCTIONS(summarise)"""
# AGGREGATION basically means we have a huge data and us huge data ma se kuch summary nikalna h


# testa=np.array([1,2,3,4])

"np.sum(array)-adds all element"
# print(np.sum(testa))

"np.mean(arr)- calcs avg"
# print(np.mean(testa))

"np.min(arr)- to find smallest val"
# print(np.min(testa))

"np.max(arr)- to find the largest val"
# print(np.max(testa))

"np.std(arr)-standard deviation"
# print(np.std(testa))

"np.var(arr)-variance"
# print(np.var(testa))



"""PRACTICE PROBLEMS"""
"PP1:Find and print the shape, size, and number of dimensions (ndim) of the array.Check the current data type (dtype).These power levels don't need decimal precision. Convert the entire array to an integer data type (astype) and print the new array"



hunter_power_levels = np.array([
    [1500.5, 3200.1], 
    [8500.0, 12450.9], 
    [55000.2, 99999.9]
])

# Write your code below:
# print(f"the shape of the array is {hunter_power_levels.shape}, its size is {hunter_power_levels.size} \nand its dimensions are {hunter_power_levels.ndim}.\nThe data type is: {hunter_power_levels.dtype}")
# newtesta=hunter_power_levels.astype(int)
# print(f"the new array is {newtesta}")

"""PP2:Find the maximum and minimum accuracy scores to see your best and worst runs.
Calculate the mean (average) accuracy of the model.
Calculate the standard deviation to see how consistent your model's performance is (a lower standard deviation means the results are more stable)."""
model_accuracies = np.array([88.5, 92.1, 85.0, 96.4, 91.2])

# Write your code below:
# print(f"the max is {np.max(model_accuracies)} and min is {np.min(model_accuracies)} while the mean is {np.mean(model_accuracies)} while the standard deviation is {np.std(model_accuracies)}")



"""PP3 : The formula for standardizing an array is:
(array - mean) / standard_deviation
Calculate the mean of the raw_data array.
Calculate the standard deviation of the raw_data array.
Use NumPy operators (+, -, /, etc.) to apply the standardization formula to the array and print the resulting "standardized" array.
"""
raw_data = np.array([10, 20, 30, 40, 50])

# Write your code below:
# print(f"the final standardised array is {(raw_data-np.mean(raw_data))/np.std(raw_data)}")

"""thats all the code for this chapter!!"""
