from tokenize import Number


number = int(input("GIVE NUMBER RIGHT NOW: "))

######
# V1 #
######
print("Version 1:")
if number / 3 == number // 3:
    print("DONE")
else:
    print("try again")

######
# V2 #
######
print("Version 2:")
if number % 3 == 0:
    print("DONE")
else:
    print("try again")

if number%3==0:
    print("Division result:",int(number/3))
else:
    print("Division result:",number/3)