#longest substring without repeating characters
def longest_substring_without_repeat_char(s):
    i = 0 
    j = 0
    char_count = {}
    max_length = 0
    while j < len(s):
        char_count[s[j]] = char_count.get(s[j],0)+1
        while char_count[s[j]] >1 and i <=j:
            char_count[s[i]] -=1
            i +=1
        max_length = max(max_length,j-i+1)
        j +=1
    return max_length 
s = "abcabcbb"
print(longest_substring_without_repeat_char(s))