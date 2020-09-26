number = float(input("Enter the number you want to check: "))


if number%2==0 and number%number == 0:
    print("Prime")
else:
    print("Not Prime")