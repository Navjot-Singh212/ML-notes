"Chapter 5 : BROADCASTING AND VECTORISATION"

import numpy as np

"BROADCASTING"
#so in the basic python we have lists and lets say we want to update all the elements of that list mathematically
#so for that we are going to need a for loop and it will a little slower this is where Broadcasting comes in handy from numpy
#basically we dont need a for loop and its faster and easier
"Broadcasting is a specific set of rules that allows you to vectorize operations even when your arrays are different shapes"
#example:
# prices= np.array([100,200,300])
# discount=10

# final_prices = prices - (prices *discount/100)
# print(final_prices)

"here is how numpy handles arrays of different shapes:"
"""
1) matching dimensions 
        ex: [1,2,3] +[4,5,6] then output will be [5,7,9]

2) expanding single elements:
        ex: [1,2,3]+10 then output will be [11,12,13]

3) Incompatible shapes 
        ex: [1,2,3] + [1,2] this will give us an error in the output          

"""

# matrix=np.array([[1,2,3],[4,5,6]])
# vector=np.array([10,20,30])
# print(matrix+vector)

# arr63=np.array([1,2])
# print(matrix+arr63)   # gives the error ValueError: operands could not be broadcast together with shapes (2,3) (2,) 

# lets see if we can solve this using reshape
# new=arr63.reshape(2,-1)    #although we put the number of columns we want instead of -1
# but -1 will make the numpy do the math(figuring out the number of columns ) all on its own
# print(matrix+new)


"Vectorisation :  performing an operation on the elements of an array all at once without loops"

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# result=arr1+arr2
# print(result)

# product=arr1*10
# print(product)


"""thats all the code for this chapter"""