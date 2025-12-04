pin = 1234
balance = 10000
trial =3
print("Welcome to the ATM")

while True:
    user_pin = int(input("Enter your pin: "))
    trial = trial - 1
    if trial > 0:
        if user_pin == pin:
            print("Please:")
            print("Enter 1 to check balance")
            print("Enter 2 to check withdraw money")
            print("Enter 3 to check add money")    
            
            choice = int(input("Enter your choice "))
            
            match choice:
                case 1:
                    print("Your current balance is: ",balance)
                    break
                case 2:
                    withdraw = int(input("Enter the amount you want to withdraw: "))
                    if withdraw <= balance:
                        print("You withdrew money. The amount you withdrew is: ", withdraw)
                        balance = balance - withdraw
                        print("Your remaining balance is: ", balance)
                        break
                    else:
                        print("Insufficient balance")
                        break
                case 3:
                    new_money = int(input("Enter the amount you want to add: "))
                    balance = balance + new_money
                    print("Your new balance is: ", balance)
                case _:
                    print("Wrong choice. Try again later. ")
                    break
            
            break
        else:
            print("You entered a wrong pin. Please try again. Trials remaining: ",trial)
    else:
        print("Your trial has ended. Try again later")
        break
    
print("Thank you for using the ATM")