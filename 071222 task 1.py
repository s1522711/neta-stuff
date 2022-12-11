import os

booklist=[]
bookpricelist=[]

def add_book(booktitle):
    print("The book named: '"+booktitle+"' was added to the cart")
    booklist.append(booktitle)

def add_book_price(bookprice):
    print("price: "+str(bookprice))
    bookpricelist.append(bookprice)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        num = int(input("How much books would you like to purchase? "))
    except ValueError:
        clear_console()
        print("Please give me a FULL number and not a string/not a full number")
        print()
        main() 
 
    loopvar=0
    while loopvar!=num:
        bookname=""
        while bookname == "":
            bookname = input("Give me the name of a book that you want to purchase: ")
            if bookname == "":
                clear_console()
                print("Please enter a book name!")
                print()
        try:
            temp=""
            while temp == "":
                temp=input("Give me the price of that book in USD: ")
                if temp == "":
                    print()
                    print("Please enter a price!")
                    print()
            bookprice = float(temp)
        except ValueError:
            clear_console()
            print("you had to give me a regular number and not a string! (for example: `2`)")
            print("Your input '"+temp+"' is incorrect")
            print("the book list has been reset, please enter everything again")
            print()
            booklist.clear()
            bookpricelist.clear()
        else:
            add_book(bookname)
            add_book_price(bookprice)
            loopvar+=1

    clear_console()

    loopvar2=0
    print("Your cart:")
    while loopvar2!=num:
        print("  "+booklist[loopvar2]+" - "+str(bookpricelist[loopvar2])+"$")
        loopvar2+=1
    print("Your total is:",str(sum(bookpricelist))+"$")
    exit(0)


clear_console()
main()