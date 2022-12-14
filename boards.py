import os

X="X"
O="O"
board1=[[X,X,X],[O,X,O],[O,O,X]]
board2=[[O,X,X],[X,O,X],[X,O,O]]
board3=[[X,X,O],[X,O,O],[X,O,X]]
board4=[[X,X,O],[O,X,X],[X,O,O]]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    BoardChoiceDone=0
    while BoardChoiceDone!=1:
        try:
            BoardChoice=int(input("Board 1,2,3 or 4? "))
        except ValueError:
            clear_console()
            print("ENTER A REGULAR NUMBER!")
        else:
            BoardChoiceDone+=1
    if BoardChoice == 1:
        BoardChoice = board1
    elif BoardChoice == 2:
        BoardChoice = board2
    elif BoardChoice == 3:
        BoardChoice = board3
    elif BoardChoice == 4:
        BoardChoice = board4

    clear_console()
    print(BoardChoice[0][0],BoardChoice[0][1],BoardChoice[0][2])
    print(BoardChoice[1][0],BoardChoice[1][1],BoardChoice[1][2])
    print(BoardChoice[2][0],BoardChoice[2][1],BoardChoice[2][2])

clear_console()
main()