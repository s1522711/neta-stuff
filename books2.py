import os

booklist=[]
pagesleftforbooks=[]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def bookpagesleft():
    currentpage=0
    totalpages=0

    currentpageentrydone=0
    while currentpageentrydone!=1:
        try:
            currentpage=int(input("On what page did you stop? "))
        except ValueError:
            print("Please enter a number!")
            print()
        else:
            currentpageentrydone=1
        
        totalpagesentrydone=0
        while totalpagesentrydone!=1:
            try:
                totalpages=int(input("What is the total amount of pages in the book? "))
            except ValueError:
                print("Please enter a number!")
                print()
            else:
                totalpagesentrydone=1
        
    pagesleftforbooks.append(totalpages-currentpage)
    clear_console()

def printfirstlastlettersinbookname(booknum):
    print("the first letter of the book `" + booklist[booknum] + "` is: `"+str(booklist[booknum][0])+"` the last letter is: `"+str(booklist[booknum][len(booklist[booknum])-1])+"`")    

def main():
    clear_console()
    currentbook=0
    totalbooks=3

    bookentryloop=0
    while bookentryloop!=totalbooks:
        print("book number:",bookentryloop+1)
        booklist.append(input("Whats the name of the book? "))
        bookpagesleft()
        bookentryloop+=1
    
    bookletterloop=0
    while len(booklist) != bookletterloop:
        printfirstlastlettersinbookname(bookletterloop)
        bookletterloop+=1

    #print(booklist)
    #print(pagesleftforbooks)

def menu():
    #clear_console()
    print()
    menuvar=""
    while True:
        menuvar=input("Enter a book number to access or `q` to quit ")
        try:
            if menuvar=="":
                print("please enter something!")
                print()
            elif menuvar=="q" or menuvar=="Q":
                exit(0)
            elif int(menuvar)==1 or int(menuvar)==2 or int(menuvar)==3:
                clear_console()
                print("Pages left to read in the book `"+booklist[int(menuvar)-1]+"` is: "+str(pagesleftforbooks[int(menuvar)-1]))
            else:
                print()
                print("please enter a book number or enter `q` to quit")
        except ValueError:
            print("you didnt enter what was requested from you!")
            print()

main()
menu()