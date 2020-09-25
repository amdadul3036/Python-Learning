# Some function are not in python by default. They should import .

import math
# x = sqrt(25)
# It's error because sqrt() function is under the math function. So we have to use like this 
x = math.sqrt(25)
print(x)
# It will print 5.0. 

# More function like this. 


# Floor 
x = math.floor(math.sqrt(12))
print(x)
# It will print 3. 


# ceil 
y = math.ceil(7.34)
print(y)
# It will print 8


# pow()
z = math.pow(2, 3)
print(z)
# It will print 8.0


# PI  . Pi is in the math function by default.
print(math.pi)


# e 
print(math.e)