# contaioner with most water
def containerwithmostwater(height):
    left =0
    right = len(height)-1
    maxarea = 0
    while left < right:
        width = right-left
        hr = min(height[left], height[right])
        current_area = width * hr
        maxarea= max(maxarea, current_area)
        if height[left]< height[right]:
            left +=1
        else:
            right -=1
    return maxarea
# Example usage:
heights = [1,8,6,2,5,4,8,3,7]
result = containerwithmostwater(heights)
print(result)