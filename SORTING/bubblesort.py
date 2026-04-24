def bubble_sort(lst):
    #for outer range loop to iterate every element
    for i in range(len(lst)):
        #for inner loop to swap element
        for j in range (len(lst)-1):
            #swap the element
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
data_list = [3,7,1,4,6,2,8,0]
print("unsorted list is : ",data_list)
sorted_list=bubble_sort(data_list)
print("the sorted list is :",sorted_list)

