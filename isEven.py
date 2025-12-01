# WAP to take a number as input and check if the number is even, odd or zero

number = int(input("Enter a number to check if it is even or not: "))
if number == 0:
    print("The number is neither even nor odd")
elif number%2  ==  0:
    print("The number you provided is even")
else:
    print("The number you provided is odd")