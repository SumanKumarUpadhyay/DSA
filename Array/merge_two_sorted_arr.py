# merge two sorted array
list1 = [6,5,7,3,4]
list2 = [9,10,8,2,1]
merge = sorted(list1+list2)
print(merge)

#2nd method 
list1 = [6,5,7,3,4]
list2 = [9,10,8,2,1]
list1.sort()
list2.sort()
i=0
j=0
list3=[]
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i=i+1
    else :
        list3.append(list2[j])
        j=j+1
list3.extend(list1[i:])
list3.extend(list2[j:])
print(list3)

