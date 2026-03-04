# Longest subarray with sum k
def longest_subarray_with_sum_k(arr,k):
    i = 0
    j = 0
    curr_sum = 0
    max_length = 0
    while j < len(arr):
        curr_sum += arr[j]
        while curr_sum > k and i <=j:
            curr_sum -= arr[i]
            i +=1
        if curr_sum == k:
            max_length = max(max_length, j-i+1)
        j +=1
    return max_length

arr = [4,1,1,1,2,3,5] 
k =5
print(longest_subarray_with_sum_k(arr,k))  