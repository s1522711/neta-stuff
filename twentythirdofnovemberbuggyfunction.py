import os
os.system("cls")


def helo():
    print("string manipulation hier:")

    string="QHello"
    if len(string)<10:
        string=string*2
    else:
        string=string+"A"
    
    if string[0]=="Q":
        string=string+"P"

    if "Hello" in string:
        print(string)
    else:
        print(string[1])

helo()

print("")

def milk():
    print("age drinks hier:")
    
    age=69

    if age==69:
        print("very old")
    elif age>18:
        print("drink coke!")
    else:
        print("drink milk!")

milk()