Score = int(input("GIVE ME YOUR FUCKING SCORE: "))

PassingScore = 55
GoodScore = 70
AmazingScore = 90

if Score == 69 or Score == 420:
    print("you got the best score!")
elif Score >= AmazingScore:
    print("you got an amazing passing score!")
elif Score >= GoodScore:
    print("you got a good passing score!")
elif Score >= PassingScore:
    print("you got a passing score")
elif Score < PassingScore:
    print("you did not get a passing score")
else:
    print("i fucked something up")