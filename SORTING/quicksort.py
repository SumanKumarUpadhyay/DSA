def quicksort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
 
        arr[j + 1] = key
        
array = [4,3,2,5,6,1,59,30]
quicksort(array)
print(array)