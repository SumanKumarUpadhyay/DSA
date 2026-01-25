def two_sum(lsit, target):
    for i in range (len(list)):
        for j in range(i+1,len(list)):
            if(list[i]+list[j])==target:
                return [i,j]
            
list = [2,4,5,6,7]
target= 10
indices = two_sum(list,target)
print(indices)


# optimal solution using hash map
def two_sum(list,target):
    hash_map = {}
    for i in range(len(list)):
        rem_need = target-list[i]
        if rem_need in hash_map:
            return [hash_map[rem_need],i]
        else:
            hash_map[list[i]] = i 
list = [2,4,5,6,7]
target= 10
indices = two_sum(list,target)
print(indices)
