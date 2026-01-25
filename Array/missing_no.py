# find missing number in array


list = [3,5,4,6,7,9]
n=len(list)
list.sort()
print(list)
start=list[0]
for i in range(n):
    if list[i]!= start + i :
        print("The missing element in this list is :",start + i)


# 2nd method but its only valid when array start from 1 
arr = [1, 2, 3, 5]

n = len(arr) + 1
expected = n * (n + 1) // 2
actual = sum(arr)

missing = expected - actual
print("Missing number:", missing)


