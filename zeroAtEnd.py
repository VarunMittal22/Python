arr=[3, 0, 1, 0, 5, 9, 0, 6, 7]
for i in range(1,len(arr)):
    if(arr[i]!=0):
        j=0
        while(arr[j]!=0):
            j=j+1
        arr[j]=arr[i]
        arr[i]=0
    print(arr)