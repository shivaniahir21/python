flag= 1
str=""
while(flag):
    if (str ==""):
        str=input("Enter a few sentences:")
    else:
        str=str+" "+input("Enter a few sentences:")
    flag=int(input("if you want to enter more type 1 else enter 0: "))

length=len(str)
spaceCount=0
alnumCount=0

for ch in str:
    if ch.isspace():
        spaceCount +=1
    elif ch.isalnum() :
        alnumCount +=1
alnumpercent=alnumCount / length * 100

print("Orignal sentences:")
print(str)

print("Number of word=",(spaceCount+1))
print("Number of characters =",(length +1))
print("Alphanumeric percentage=",alnumpercent)
