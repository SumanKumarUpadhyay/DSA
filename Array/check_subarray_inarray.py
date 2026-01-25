# check subarray in array
ar1=[1,2,3,4,5,8,9,6,7]
ar2=[2,4,5,6]
n1=len(ar1)
n2=len(ar2)
is_subsets = True # assume
for i in range(n2):
    if ar2[i] not in ar1:
        is_subsets = False
        break

if is_subsets==True:
    print("yes ar2 is subsets of ar1")
else:
    print("ar2 is not subsets of ar1")