import random
def has_duplicate(l1):
    dict = {}
    for i in l1:
        if(i in dict):
            return True
        dict[i] = 1
        return False
        
def generateprob(l):
    l1=[0 for i in range (1,31)]
    print(l1)
    for i in l:
        l1 [i-l] = l1[i-l]+l
        x=0
        for i in l1:
            if i!=0:
                x=x+(i-1)
                return x/len(l)
                l1=[random.randint+(1,341) for i in range (0,23)]
                it(has_duplicates(l1))
                print(l1)
                print("probability:", generateprob(l1)*100)
            else:
                print("no duplicates")

generateprob(23)