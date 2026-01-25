def two_sum(list,target):
    hash_map={}
    for i in range(len(list)):
        rem_need = target - list[i]
        if rem_need in hash_map:
            return [hash_map[rem_need],i]
        else:
            hash_map[list[i]]=i

list = [2,5,8,0]
target = 8
indices=two_sum(list,target)
print(indices)
