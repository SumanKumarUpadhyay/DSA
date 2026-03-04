#Maximum of all subarrays of size k 
def max_of_subarrays(arr,k):
    n = len(arr)
    if n<k:
        return []
    result = []
    for i in range(n - k + 1):
        window = arr[i:i+k]
        result.append(max(window))
    return result
# example usage
arr = [2,1,5,1,3,2]
k = 3
print(max_of_subarrays(arr,k))
