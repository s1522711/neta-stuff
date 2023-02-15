import os

os.system('cls' if os.name == 'nt' else 'clear')

first = input("What is your first name? ")
last = input("What is your last name? ")

print(first.capitalize(),last.capitalize())