# Lists and arrays are used in Python to store data(any data type- strings, integers etc), both can be indexed and iterated also. Difference between lists and arrays are the functions that you can perform on them like for example when you want to divide an array by 4, the result will be printed on request but in case of a list, python will throw an error message. Here's how it works: 


from numpy import array
a = array([4,8,16,20])
a = a/4
print(a)