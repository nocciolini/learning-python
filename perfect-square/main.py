number = float(input("Input a number: "))
sqrt = float(number ** 0.5)

if sqrt.is_integer():
    print("The number is a perfect square:", number)
else:
    print("The number is not a perfect square:", number)
