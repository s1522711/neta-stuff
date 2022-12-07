# Change this list - try different inputs
grades = [81, 70, 75, 96, 99, 100, 87, 80, 100]
print("Testing the following grades list:", grades)
print("**************************************")

# DO NOT CHANGE THIS LINE:
print("Your solution: ", end="")

# Write your solution here:

sumofgrades = sum(grades)
amountofgrades = len(grades)
avrageofgrades = sumofgrades/amountofgrades
result = avrageofgrades in grades
print(result)








# DO NOT CHANGE:
#import sol
#print("The correct solution:", sol.solve(grades))