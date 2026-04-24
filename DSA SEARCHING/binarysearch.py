# binary search algorithm 
def binary_search(arr, target):
    left, right = 0 , len(arr) - 1
    while left<= right:
        mid = (left + right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target :
            left = mid + 1
        else:
            right = mid -1
    return False
# example usage
arr = [1, 2, 3, 4, 5]
target = 4
result = binary_search(arr, target)
if result is not False:
    print(f"Element found at index: {result}")
else:
    print("Element is not found")

        
        

        
       