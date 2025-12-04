# Take any two numbers from user, and add, subtract, multiply, and divide those numbers and print the output along 
# with a message
# also, print the square and cube of the two numbers entered by the user

firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter another number: "))

print("Addition: ",firstNumber+secondNumber)
print("Subtraction: ", firstNumber-secondNumber)
print("Multiplication: ", firstNumber*secondNumber)
print("Division: ",firstNumber//secondNumber)
print("Remainder: ",firstNumber%secondNumber)

print("Square of first number = ",firstNumber**2)
print("Square of second number = ",secondNumber**2)

print("Cube of first number = ",firstNumber**3)
print("Cube of second number = ", secondNumber**3)