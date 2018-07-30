import random
def add(num1,num2):
    print(num1, "+" ,num2 , "= ")
    res = input()
    ans = num1+num2;
    print(ans)
    print("res = ",res)
    if res == ans:
        print("correct")
    else:
        print("wrong")


def sub(num1, num2):
    print(num1, "-", num2, "= ")
    res = input()
    ans = num1 - num2;
    if res == ans:
        print("correct")
    else:
        print("wrong")

for i in range(1,100):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    opr = [add(num1,num2), sub(num1,num2)]
    random.choice(opr)

