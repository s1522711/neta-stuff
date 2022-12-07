x = 100
cases = {100:"Big",50:"Medium",10:"Small"}
for case in cases:
    if x >= case[0]:
        print(case[1])
        break