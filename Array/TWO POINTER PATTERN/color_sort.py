def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:  # arr[mid] == 'B'
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
# Example usage:
arr = ['G', 'B', 'R', 'R', 'B', 'G', 'R']
sorted_arr = sort_colors(arr)
print(sorted_arr)