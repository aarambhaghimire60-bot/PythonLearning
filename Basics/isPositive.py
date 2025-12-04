# WAP to take a number from user as an input and check if the number is positive, negative or zero
number = int(input("Enter a number to check if it is positive, negative or zero: "))

if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")