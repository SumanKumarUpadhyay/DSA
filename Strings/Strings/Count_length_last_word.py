# count last word of a string
def count_length_last_word(s):
    for  i in range(len(s)-1,0,-1):
        if s[i]==' ':
            return len(s[i+1:])
        
s = "hello World"
print(count_length_last_word(s))

# optimal solution
def count_length_last_word(s):
    length = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            length +=1
        else:
            break
    return length
s = "hello World"
print(count_length_last_word(s))