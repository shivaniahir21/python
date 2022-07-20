def add_student(name):
    with open('student.txt','a') as file:
        file.write(name)

def find_student(name):
    with open('student.txt', 'r') as file:
        for n in file.readlines():
            if n.lower().split(' ')[0] ==  name.lower():
                return n
    return ''

def show_stduent():
    with open('student.txt', 'r') as file:
        print(file.readlines())


name = input('Enter Name of Student:')
add_student(f"\n{name}")
print("File Data:")
show_stduent()

name = input("Enter Name of Student to be search:")
fullName = find_student(name);
if  fullName!= '':
    print("Full Name Of Student: ", fullName)
else:
    print("Name not found")