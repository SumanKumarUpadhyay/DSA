# inseertion sort algorithm '
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>=0 and key < list[j]:
            list[j+1] = list[j]
            j -=1
        list[j+1] = key
list = [3,7,1,4,6,2,8,0]
print("unsorted list is : ",list)
insertion_sort(list)
print("the sorted list is :",list)