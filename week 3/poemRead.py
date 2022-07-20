def readPoem():
    with open('poem.txt','r') as file:
        for line in file.readlines():
            print(line,end='')

print("Poem:\n")
readPoem()
