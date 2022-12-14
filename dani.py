import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    InputQuestion = input("What question do you want to ask dani? ")

    
    if InputQuestion.endswith("?!") or InputQuestion.endswith("!?"):
        print("Calm down, I know what i'm doing!")
    elif InputQuestion.endswith("?"):
        print("Sure")
    elif InputQuestion.endswith("!"):
        print("Whoa, chill out!")
    else:
        print("Whatever")

clear_console()
main()