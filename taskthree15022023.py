import os

os.system('cls' if os.name == 'nt' else 'clear')

lst = []

def main():
    for x in range(1,50):
        if x % 7 == 0:
            print("Boom!")
        else:
            print(x,end=" ")

main()