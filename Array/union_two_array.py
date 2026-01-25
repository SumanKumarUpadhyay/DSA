ar1=[3,4,5,6,9]
ar2=[3,5,8,9]
n1=len(ar1)
n2=len(ar2)
arr3=[]
for i in  range(n1):
    if ar1[i] not in arr3:
        arr3.append(ar1[i])

for j in range(n2):
    if ar2[j] not in arr3:
        arr3.append(ar2[j])

print(arr3)
