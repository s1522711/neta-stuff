import os

os.system('cls' if os.name == 'nt' else 'clear')

number = int(input("Give me a number: "))
for x in range(-20,number):
    if x % 5 == 0:
        print(x)
