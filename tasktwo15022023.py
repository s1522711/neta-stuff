import os

os.system('cls' if os.name == 'nt' else 'clear')

for x in range(1,51):
    if x % 8 == 0:
        print(x,"nice")
    else:
        print(x)