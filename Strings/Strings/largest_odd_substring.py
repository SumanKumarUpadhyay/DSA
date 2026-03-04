# we have to find largest substring in string which is odd
def largest_odd_substring(s):
    for i in range(len(s)-1,0,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
s = "123456"
print(largest_odd_substring(s))