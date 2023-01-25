import random
ZeMax = int(input("give me the maximum number for this: "))
a=9999999999999999
b=9999999999999999
c=9999999999999999
while a not in range(0,ZeMax):
    a=random.randint(0,ZeMax)
while b not in range(0,ZeMax):
    b=random.randint(0,ZeMax)
while c not in range(0,ZeMax):
    c=random.randint(0,ZeMax)

print(a,"+",b,"=",c)