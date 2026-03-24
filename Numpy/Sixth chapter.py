"Chapter 6 : HANDLING MISSING AND SPECIAL VALUES"
"""
three functions of numpy that helps with missing values:

np.isnan() : detect missing values

np.nan_to_num() : to replace the missing values with some other number/value

np.isinf() : used to detect infinte values

where nan stands for not a number
"""

import numpy as np

"np.isnan(array)"
# arr=np.array([1,2,np.nan,4,np.nan,6])

# print(arr)
# print(np.isnan(arr))        # this will give true for the values that are nan and false fo values that are non-nan

# NOTE : you cannot directly compare nan values example: np.nan==np.nan 

"np.nan_to_num(array,nan=value)  by default nan=0"
# cleanarr1=np.nan_to_num(arr)
# print(cleanarr1)

# print(np.nan_to_num(arr,nan=65))



"np.isinf(array) for values that exceed the storage limit of python such as 10^100000 or 1/0"

# arr=np.array([1,2,np.inf,4,-np.inf,6])
# print(np.isinf(arr))        # returns boolen values aka true for infinite values and false for finite numbers

#now to replace inf with some value:

# cleanedarr= np.nan_to_num(arr,posinf=1000,neginf=-1000)
# print(cleanedarr)

"thats all the code for this chapter!!!"