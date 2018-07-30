neg=[]
sub=[]
sum=0
arr=[5,-6,8,-2,-4,-2]
for i in range(0,len(arr)):
     for j in range(i,len(arr)):
          sum=sum+arr[j];
          neg.append(arr[j])
          if sum==0:
              sum = 0
              sub.append(neg)
              neg = []
     sum=0
     neg=[]
print(sub)