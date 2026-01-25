list = [1,3,4,5,5,5,9,8,8,6]
result = (set(list))
print(result)

# 2nd method
def rep_check(list):
    duplicates=[]
    for i in range(1,len(list)):
        if list[i-1]==list[i]:
            duplicates.append(list[i])
    return duplicates
        

list = [1,3,4,5,5,9,8,8,6]
list.sort()
print(rep_check(list))
