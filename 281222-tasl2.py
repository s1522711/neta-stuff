import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

StudentsCame=0

clear_console()
StudentAmountEntryDone=0
while StudentAmountEntryDone==0:
    try:
        StudentsCame=float(input("How Many Students Came to this activity? "))
    except ValueError:
        print()
        print("Give me a regular number!")
    else:
        StudentAmountEntryDone+=1

clear_console()
if StudentsCame>30:
    print("You're great instructors!")
elif StudentsCame<=30 and StudentsCame>20:
    print("the amount of students in the tribe is the biggest it has ever been!")
elif StudentsCame<=20 and StudentsCame>10:
    print("the amount of students in the tribe is good!")
elif StudentsCame<=10:
    print("Recruit more students to the tribe NOW!")
else:
    print("ive fucked something up!")

print("this is the best boyscouts tribe in israel!")