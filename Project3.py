# Print all numbers from 1 to 300 which are not divisible by 3 and 5
# In project2 we have done it by using for loop and if statement . Here we will do it it
# using continue. 


for i in range(1 , 201):
    if i%3==0:
        continue
    if i%5==0:
        continue
    print(i)
    
# So continue means something that skip it and go to down and do your work. Just skip it. 