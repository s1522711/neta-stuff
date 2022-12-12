import os
import time

debugentrydone=0
while debugentrydone!=1:
    try:
        debuglevel=int(input("is this a debug run? 1 or 0: "))
        if debuglevel==1 or debuglevel==0:
            debugentrydone=1
        else:
            print("you had to enter `1` or `0`!")
    except ValueError:
        print("you had to enter `1` or `0`!")

booklist=[]
bookpricelist=[]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_console()
    numdone=0
    while numdone!=1:
        try:
            num = int(input("How much books would you like to purchase? "))
        except ValueError:
            print("you had to give me a regular number and NOT a string!")
        else:
            numdone=1
    
    bookentryloopvar=0
    while bookentryloopvar!=num:
        if debuglevel==1:
            print(bookentryloopvar)
        bookname=""
        while bookname=="":
            print()
            bookname = input("Give me the name of a book that you would like to puchase: ")
            print()
            if bookname == "":
                clear_console()
                print("You have to give me a book name!")

        priceentrydone=0
        while priceentrydone!=1:
            try:
                bookprice = float(input("Give me the price of that book: "))
            except ValueError:
                clear_console()
                print("You had to give me the price of the of the book in regular numbers without any symbols!")
                print()
            else:
                booklist.append(bookname)
                bookpricelist.append(bookprice)
                bookentryloopvar+=1
                priceentrydone=1
    
    clear_console()
    bookprintloopvar=0
    print("Your cart:")
    while bookprintloopvar!=num:
        print ("  "+booklist[bookprintloopvar]+" - "+str(bookpricelist[bookprintloopvar])+"$")
        if debuglevel==1:
            time.sleep(1)
        bookprintloopvar+=1
    print("Your total is:",str(sum(bookpricelist))+"$")




main()
exit(0)