def readStory():
    with open('story.txt','r') as file:
        for line in file.readlines():
            print(line,end='')
def countLine():
    count=0
    with open('story.txt','r') as file:
        for line in file.readlines():
            if line[0].lower() != 't':
                count+=1
    return count

print("Story:\n")
readStory()

print("\n\nNumber of lines started without \'T\' : ", countLine())
