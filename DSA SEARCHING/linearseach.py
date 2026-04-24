# linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return False
# example usage
arr = [1, 2, 3, 4, 5]
target = 0
result = linear_search(arr, target)
if result is not False:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
