principle=int(input("Enter Priciple Amount : "))
rate=float(input("Enter Rate : "))
time=int(input("Enter Time : "))
simple_interest=(principle*rate*time)/100
print("Simple Interest =",simple_interest )
amount=principle + simple_interest
print("Amount = ",amount)