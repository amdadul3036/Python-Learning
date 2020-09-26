number = int(input("Enter the number you want to check: "))

for i in range(2 , number):
    if number%i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
    
# Here is the use of for else . 