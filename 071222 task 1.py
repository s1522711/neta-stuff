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
        num = float(input("How much books would you like to purchase? "))
    except ValueError:
        clear_console()
        print("you had to give me a regular number and not a string! (for example: `2`)")
        print("Please run the program again")
        print()
        main()
        
 
    loopvar=0
    while loopvar!=num:
        bookname = input("Give me the name of a book that you want to purchase: ")
        try:
            bookprice = float(input("Give me the price of that book in USD: "))
        except ValueError:
            clear_console()
            print("you had to give me a regular number and not a string! (for example: `2`)")
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
    #print("")
    print("Your total is:",str(sum(bookpricelist))+"$")
    exit(0)


clear_console()
main()

