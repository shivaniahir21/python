count=0
with open('words.txt', 'r') as file:
    for char in file.read():
        if char.isupper():
            count+=1

print(count)
