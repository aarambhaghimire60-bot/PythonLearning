# match can be used where ever if else can be

day = int(input("Enter a number from 1 to 7: "))

match day:
    case 1:
        print("Today is Sunday")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("You entered a wrong number. Please enter a number between 1 to 7 in the next try")