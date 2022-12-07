import os
os.system("cls")

booklist=[]
bookpricelist=[]
def add_book(booktitle):
    print("The book named: '"+booktitle+"' was added to the cart")
    booklist.append(booktitle)



def add_book_price(bookprice):
    print("price: "+str(bookprice))
    bookpricelist.append(bookprice)




def main():
    num = int(input("How much books would you like to purchase? "))
    loopvar=0

    while loopvar!=num:
        bookname = input("Give me the name of a book that you want to purchase: ")
        bookprice = int(input("Give me the price of that book in USD: "))
        add_book(bookname)
        add_book_price(bookprice)
        loopvar+=1

    os.system("cls")

    loopvar2=0
    print("Your cart:")
    while loopvar2!=num:
        print(" "+booklist[loopvar2]+" -",str(bookpricelist[loopvar2])+"$")
        loopvar2+=1
    print("")
    print("Your total is:",str(sum(bookpricelist))+"$")


main()

