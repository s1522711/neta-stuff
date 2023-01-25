def main(st):
    result=""
    count=1
    for i in range(1,len(st)):
        if st[i] == st[i-1]:
            count+=1
        else:
            result=str(st[i-1])+" "+str(count)
    return result

print(main(input("give me a string: ")))
