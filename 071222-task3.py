import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

age=0

clear_console()
EntryDone=0
while EntryDone==0:
    try:
        age = int(input("Whats your age? "))
    except ValueError:
        print()
        print("Please enter a number!")
        print()
    else:
        EntryDone+=1

TicketAmount=0

clear_console()
if age<=18:
    print("You are Eligable for a YOUTH tickets - 1 ticket is 40ILS")
elif age>18:
    print("You are only eligable for a ADULT ticket - 1 ticket is 60ILS")

SecondEntryDone=0
while SecondEntryDone==0:
    try:
        TicketAmount = int(input("Whats the amount of tickets that you want to buy? "))
    except ValueError:
        print()
        print("Please enter a number!")
        print()
    else:
        SecondEntryDone+=1

clear_console()
if age<=18:
    print("you are buying "+str(TicketAmount),"YOUTH tickets")
    print("your total is: "+str(TicketAmount*40)+"ILS")
elif age>18:
    print("you are buying "+str(TicketAmount),"ADULT tickets")
    print("your total is: "+str(TicketAmount)+"ILS")
