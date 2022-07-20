phNo =input("ENTER THE PHONE NUMBER:")
length = len(phNo)

if length == 12 \
    and phNo[3]=="_" \
    and phNo[7]=="_" \
    and phNo[:3].isdigit()\
    and phNo[4:7].isdigit()\
    and phNo[8].isdigit():
        print("Valid phone number")
else:
    print("Invalid phone numbe")
     
