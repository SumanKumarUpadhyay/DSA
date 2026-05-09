# find first uniwue character in a string
def first_unique_char(s):
    hp = {}
    for char in s:
        if char in hp:
            hp[char] +=1
        else:
            hp[char]=1
    for char in s:
        if hp[char] == 1:
            return char
    return None
s = "leetcode"
print(first_unique_char(s))

# first unique character index in string
def first_unique_char_index(s):
    hp={}
    for char in s:
        if char in hp:
            hp[char]+=1
        else:
            hp[char]=1
    for i in range(len(s)):
        if hp[s[i]]==1:
            return i
    return -1
s = "loveleetcode"
print(first_unique_char_index(s))
