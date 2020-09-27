# array_input_from_user.py

from array import *

arr = array('i' , [])

n = int(input("Enter the number of element you want to insert into the array: "))

for k in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
print(arr)