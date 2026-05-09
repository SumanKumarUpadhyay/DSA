# implemet ransom magazine in python
def canConstruct(ransomNote:str, magazine:str) -> bool:
    # create a hash map to store the count of each character in the magazine
    char_count = {}
    
    # iterate through the magazine and count the characters
    for char in magazine:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # iterate through the ransom note and check if the characters are available in the magazine
    for char in ransomNote:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False
            
    return True

ransomNote = "aa"
magazine = "ba"
print(canConstruct(ransomNote, magazine)) # True