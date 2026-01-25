def leader_array(arr):
    leader = []
    n = len(arr)
    max_from_right = arr[n-1]
    leader.append(max_from_right)
    for i in range(n-2,-1,-1):
        if arr[i]>max_from_right:
            max_from_right = arr[i]
            leader.append(max_from_right)
    leader.reverse()
    return leader
# Example usage:
arr = [16, 17, 4, 3, 5, 2]
print(leader_array(arr))  