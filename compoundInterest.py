p = int(input("enter principal: "))
r = int(input("enter annual interest rate: "))
t = int(input("enter time interval: "))
rate = 1+(r/100)
temp = rate**t
amt = p*temp
print("amount = ",amt)