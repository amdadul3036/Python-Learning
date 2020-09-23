# For every variable value have a different id number. 


a = 10 
print(id(a))
print(id(10))


b = 10
print(id(b))

# a = c 
# It's not defined a = c . but c = a is defined.
c = a
print(id(c))

# All of the above's id is smae. Because everyone consists of same value 10 . 
# Id will change if and only if the value is change. 


c = 19
print(id(c))



'''
So the id will be different only when value is different. 
We can consider the id as a box . For every value there is a different box in python.
Such as for 10 there is a box. a,b,c are calling this same box. And last c is calling
another box of 19. 
'''