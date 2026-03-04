# maximum Sum Subarray of size k
def max_sum_subarray(arr,k):
    n = len(arr)
    if n < k:
        return -1
    max_sum = 0
    window_size_sum = sum(arr[:k])
    max_sum = window_size_sum
    for i in range(k,n):
        window_size_sum += arr[i]-arr[i-k]
        max_sum = max(max_sum,window_size_sum)
    return max_sum
# example usage 
arr = [2,1,5,1,3,2]
k = 3
print((max_sum_subarray(arr,k)))  
