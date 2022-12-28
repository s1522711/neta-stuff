import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

price=0

clear_console()
EntryDone=0
while EntryDone==0:
    try:
        price = float(input("Whats the price of the gym pass? "))
    except ValueError:
        print()
        print("Please enter a number!")
        print()
    else:
        EntryDone+=1

clear_console()
if price<150:
    print("Amazing Price!")
elif price>=150 and price<=250:
    print("Good Price!")
elif price>250:
    print("Expencive but good!")
else:
    print("Ive fucked something up!")

print("Thanks for using Ehud and David's price checking program!")