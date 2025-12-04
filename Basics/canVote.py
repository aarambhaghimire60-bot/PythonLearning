# take the user's age as input and print if the user can vote or not
age = int(input("Please tell me your age: "))

#  age >= 18? If yes, then they can vote => Yes/No => True/False => 1/0
#  age < 18? If yes, then the cannot vote => Yes/No => True/False => 1/0

# Conditionals => if else condition
if age >= 18:
    # indentation: harek : sign pachi enter garda automatically 4 spaces (1 tab) ko gap banera aauxa
    print("You can vote")
else:
    print("You cannot vote")