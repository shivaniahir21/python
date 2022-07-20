from pickle import LIST


def remove_duplicates(list):
    distinctList =[]
    for i in range(0, len(list)):
        if list[i] not in distinctList:
            distinctList.append(list[i])
    return distinctList
    
list = []
while True:
    var = input("Enter element [X for exit]:")
    if var=='X':
        break
    list.append(var)

print("Original List:", list)
print("List after removing duplicates:", remove_duplicates(list))