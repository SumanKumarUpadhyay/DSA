arr=(1,4,-3,9,0)
n=len(arr)
# we have add -3 and 9 
if n==1:
    print(arr[0])

max=0
min=0

for i in range(0,n):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
print(max+min)
    


