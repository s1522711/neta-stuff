import os
import time
import random





#animlevel=random.randint(0, 1)
#print(animlevel)



booklist=[]
bookpricelist=[]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_console()
    numdone=0
    while numdone!=1: #amount of books
        try:
            num = int(input("How much books would you like to purchase? "))
        except ValueError:
            print("you had to give me a regular number and NOT a string!")
        else:
            numdone=1
    
    bookentryloopvar=0
    while bookentryloopvar!=num: #book name entry
        bookname=""
        while bookname=="":
            print()
            bookname = input("Give me the name of book number "+str(bookentryloopvar+1)+": ")
            print()
            if bookname == "":
                clear_console()
                print("You have to give me a book name!")


        priceentrydone=0
        while priceentrydone!=1: #book price entry
            try:
                bookprice = float(input("Give me the price of book number "+str(bookentryloopvar+1)+": "))
            except ValueError:
                clear_console()
                print("You had to give me the price of the of the book in regular numbers without any symbols!")
                print()
            else:
                booklist.append(bookname)
                bookpricelist.append(bookprice)
                bookentryloopvar+=1
                priceentrydone=1
    
    animlevel=1
    SetAnimLevelDone=0
    if bookname.endswith("`") and SetAnimLevelDone == 0:
        animlevel=0
        SetAnimLevelDone=1
    
    clear_console()
    #print(animlevel)
    bookprintloopvar=0
    print("Your cart:") #animated cart printing
    while bookprintloopvar!=num:
        if animlevel==1:
            time.sleep(0.3)
        if bookpricelist[bookprintloopvar] % 1 == 0:
            print ("  "+booklist[bookprintloopvar]+" - "+str(int(bookpricelist[bookprintloopvar]))+"$")
        else:
            print ("  "+booklist[bookprintloopvar]+" - "+str(bookpricelist[bookprintloopvar])+"$")
        bookprintloopvar+=1
    
    
    if sum(bookpricelist) >= 50: #slow cart total print if total >= 50
        if animlevel==1:
            time.sleep(0.3)
            print("loading...")
            time.sleep(2)
        
        clear_console() #reprint cart with no line print delay
        bookprintloopvar=0
        print("Your cart:")
        while bookprintloopvar!=num:
            if bookpricelist[bookprintloopvar] % 1 == 0:
                print ("  "+booklist[bookprintloopvar]+" - "+str(int(bookpricelist[bookprintloopvar]))+"$")
            else:
                print ("  "+booklist[bookprintloopvar]+" - "+str(bookpricelist[bookprintloopvar])+"$")
            bookprintloopvar+=1
        
        if sum(bookpricelist) % 1 == 0: #print cart total
            print("Your total is:",str(int(sum(bookpricelist)))+"$")
        else:
            print("Your total is:",str(float(sum(bookpricelist)))+"$")
    
    
    else:         # fast cart total print if total < 50
        if animlevel==1:
            time.sleep(0.5)
        if sum(bookpricelist) % 1 == 0:
            print("Your total is:",str(int(sum(bookpricelist)))+"$")
        else:
            print("Your total is:",str(float(sum(bookpricelist)))+"$")
    if animlevel==1:
        time.sleep(0.3)




main()
exit(0)