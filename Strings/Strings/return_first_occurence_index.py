# return first occurence index
def return_first_occurence_index(heystack,needle):
    for i in range(len(heystack)):
        if heystack[i:i+len(needle)] == needle:
            return i
    return -1
heystack = "suman kumar"
needle = "kumar"
print(return_first_occurence_index(heystack,needle))