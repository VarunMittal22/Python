grLst=[]
rate=[]
num = int(input("enter how namy items u want to insert: "))
for i in range(1,num+1):
    gro= input("enter the grocery item: ")
    grLst.append(gro)
    r= input("enter amouunt as per kg: ")
    rate.append(r)
print(grLst)
print(rate)
size = len(grLst)
print(size)
flag=1
ser= input("enter the grocery item u want to search: ")
for i in range(1,size):
    if(ser == grLst[i]):
        print("amount of "+ser, "is " + rate[i])
        flag=0
if(flag==1):
    print("Invalid search")

