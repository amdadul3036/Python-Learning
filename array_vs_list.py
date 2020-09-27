# In list you can use any data type together but in array you have to use same data type elements. 

from array import *

val = array( "i" , [2,-4,6,2,8,5])
print(val)
print(val.buffer_info())

# Printing all values of an array. 
for p in val:
    print(p)

val1 = array( "I" , [2,4,6,2,8,5])
print(val1)



# For characters you should use "u". U for unique . 
val2 = array('u' , ['A' , 'm' , 'd' , 'a' , 'd' , 'u' , 'l'])
print(val2)