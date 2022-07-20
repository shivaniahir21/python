def bubble_sort(list):
    length = len(list)
    for i in range (0, length-1):
        for j in range(length-1):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

list = [9,56,45,1,9,6,66]
print("Unsorted List:",list)
print("Sorted List:",bubble_sort(list))
