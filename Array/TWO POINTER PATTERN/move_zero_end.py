arr = [0,1,0,3,12,0,5]
n = len(arr)
j = 0 
for i in range(n):
    if arr[i]==0:
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j +=1
print(arr)
