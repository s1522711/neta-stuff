import os


numbers = []
def sort():
    numbers.sort()
    print(*numbers, sep=", ")
    print("The smallest number is:",numbers[0])
    print("The biggest number is:",numbers[len(numbers)-1])

numbers_entry_loop=0
while numbers_entry_loop<5:
    try:
        entered_number=float(input("Give me number "+str(numbers_entry_loop+1)+": "))
    except ValueError:
        print("Enter A Fucking Number!")
    else:
        if entered_number % 1 == 0:
            numbers.append(int(entered_number))
        else:
            numbers.append(entered_number)
        numbers_entry_loop+=1
os.system('cls' if os.name == 'nt' else 'clear')
sort()