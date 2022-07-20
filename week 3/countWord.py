def readWord():
    with open('words.txt','r') as file:
        for line in file.readlines():
            print(line,end='')

def countWord():
    count=0
    with open('words.txt','r') as file:
        for line in file.readlines():
            count+= len(line.split(' '))
    return count

print("File:\n")
readWord()

print("\n\nNumber of words in file: ", countWord())
