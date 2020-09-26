# Print first 50 Fibonacci Number


first = 0
second = 1
for i in range(0 , 50):
    third = first + second
    first = second
    second = third
    print(third)
    



# It's wrong but why?