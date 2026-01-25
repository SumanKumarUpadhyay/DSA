# reverse the strings
# method 1 
s = "suman"
rev_string=s[::-1]
print(rev_string)

# 2 method 
s = "Komal"
s = list(s)           # Convert string to list of characters
left, right = 0, len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

s = "".join(s)        # Convert list back to string
print(s)

# 3rd method 
s = "suman"
rev_string = "".join(reversed(s))
print(rev_string)

