def is_sort(list):
    valid = True
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


list = []
while True:
    var = input("Enter element [X for exit]:")
    if var=='X':
        break
    list.append(var)

print("List:", list)
print(" is Sorted" if is_sort(list) else "is not sorted")