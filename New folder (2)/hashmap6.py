# anagram checker using hashmap
def anagram(str1, str2):
    char_count = {}
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1
    for char in str2:
        if char in char_count:
            char_count[char] -=1
        else:
            return False
    #for value in char_count.values():
    #    if value !=0:
    #        return False
    return True
str1 = "listen"
str2 = "silent"
print(anagram(str1, str2))