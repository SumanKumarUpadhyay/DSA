arr = [3,5,-3,0,-6,9,-1]
n = len(arr)
j = 0 
for i in range(n):
    if arr[i]<0:
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j +=1
print(arr)