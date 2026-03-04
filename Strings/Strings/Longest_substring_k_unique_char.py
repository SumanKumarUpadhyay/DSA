# Longest substring with k unique characters
def longest_substring_k_unique_char(s,k):
    i = 0
    j=0
    char_count = {}
    max_length = 0
    while j < len(s):
        char_count[s[j]] = char_count.get(s[j],0)+1
        while len(char_count) > k and i<=j:
            char_count[s[i]] -= 1
            if char_count[s[i]] == 0:
                del char_count[s[i]]
            i +=1
        if len(char_count) == k :
            max_length = max(max_length, j-i+1)
        j +=1
    return max_length
s = "aabacbebebe"
k = 3
print(longest_substring_k_unique_char(s,k))