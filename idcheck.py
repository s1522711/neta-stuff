idnum = input("Give me an id number: ")
post_x2 = idnum[0]+str(int(idnum[1])*2)+idnum[2]+str(int(idnum[3])*2)+idnum[4]+str(int(idnum[5])*2)+idnum[6]+str(int(idnum[7])*2)
sum_of_id = str(sum(int(digit) for digit in str(post_x2)))
check_digit = 0
if int(sum_of_id[len(sum_of_id)-1]) >= 5:
    for x in range(0,5):
        if (int(sum_of_id)+x) % 10 == 0:
            check_digit = x
else:
    for x in range(0,4):
        if (int(sum_of_id)-x) % 10 == 0:
            check_digit = x
#print(check_digit)
#print(idnum[8])
print(int(check_digit) == int(idnum[8]))