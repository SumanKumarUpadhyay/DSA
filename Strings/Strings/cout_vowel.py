str1 = 'suman'
vowels = 'aeiou'
count = 0 
for char in str1:
    if char in vowels:
        count +=1

print("Number of vowels in the string:", count)