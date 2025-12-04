# Simple Interest = (Principle * Time * Rate) / 100
principle = int(input("Enter Principle Amount: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter Time: "))

simple_interest = (principle*rate*time)/100

print("Simple Interest = ", simple_interest)