print("select option")
print("1.Add")
print("2.sub")
print("3.mul")
print("4.div")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

ch = input("enter choice:")
num1 = int(input("enter num 1:"))
num2 = int(input("enter num 2:"))


if ch == '1':
    print(add(num1,num2))

elif ch == '2':
    print(sub(num1,num2))

elif ch =='3':
    print(mul(num1,num2))

elif ch =='4':
    print(div(num1,num2))

else:
    print("Invalid Input")


