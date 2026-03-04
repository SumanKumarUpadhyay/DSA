# valid Anagram , means two strings have same characters with same frequency
s1 = "anagram"
s2 = "nagrama"
if sorted(s1)==sorted(s2):
    print("valid anagram")

# optimal solution using hashmap
def valid_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for char in s1:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    for char in s2:
        if char in count:
            count[char]-=1
        else:
            return False
    for k in count:
        if count[k]!=0:
            return False
    return True
s1 = "anagram"
s2 = "nagraaa"
print(valid_anagram(s1,s2))