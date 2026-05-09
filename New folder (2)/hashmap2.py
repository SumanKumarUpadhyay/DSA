# given a string print the word with frequency k 
def word_freq_k(s,k):
    hp = {}
    for char in s :
        if char in hp:
            hp[char] += 1
        else:
            hp[char]= 1
    chars = []
    for char in hp:
        if hp[char] == k:
            chars.append(char)
    return chars

s = "aabbbccd"
k = 2
print(word_freq_k(s,k)) # ['l']