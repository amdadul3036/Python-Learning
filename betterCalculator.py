num1 = float(input("Inter First Number: "))
operator = input("Inter Operator: ")
num2 = float(input("Inter Second Number: "))


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
else:
    print(num1/num2)