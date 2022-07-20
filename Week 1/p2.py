def feet_to_inch(feet):
    inch= 12*feet
    return inch

def inch_to_feet(inch):
    feet= inch/12
    return feet

feet= int(input("ENTER NO OF FEET: "))
inch= feet_to_inch(feet)
print(inch)

newinch=int(input("ENTER NO OF INCH: "))
newfeet= inch_to_feet(newinch)
print(newfeet)
    
        
    
