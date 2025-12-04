total_money = 10000
pin = 1234

print("Welcome to our ATM ")
user_pin = int(input("Please enter your PIN "))

if user_pin == pin:
    cash_withdraw = int(input("Enter the amount you want to withdraw: "))
    if cash_withdraw > total_money:
        print("Insufficient balance")
        exit
    else:
        total_money = total_money -  cash_withdraw
        print("Withdrawal successful")
        print("Remaining balance= ", total_money)
        
else:
    print("Your PIN is incorrect. Try again!!!")