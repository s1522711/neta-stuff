import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

BookList=[]
BookPriceList=[]

def main():
    clear_console()
    
    BookAmountEntryDone=0
    while BookAmountEntryDone!=1:
        try:
            BookAmount=int(input("How many books would you like to purchase? "))
        except ValueError:
            print("Please Enter A Regular Number!")
            print()
        else:
            if BookAmount!="" and BookAmount!=0:
                BookAmountEntryDone+=1
            else:
                print("Please Enter A Normal Number!")
                print()

    
    clear_console()

    CurrentBookNumber=0
    while CurrentBookNumber!=BookAmount:
        BookName=""
        while BookName=="":
            BookName=input("Please enter the name of book "+str(CurrentBookNumber+1)+":")
            if BookName=="":
                print("Please Enter The Name Of The Book!")
                print()
            else:
                BookList.append(BookName)
        
        BookPrice=0
        BookPriceEntryDone=0
        while BookPriceEntryDone==0:
            try:
                BookPrice=float(input("Please Enter The Price Of Book "+str(CurrentBookNumber+1)+":"))
            except ValueError:
                print("Please Enter A Number!")
                print()
            else:            
                if BookPrice=="":
                    print("Please Enter The Price Of The Book In USD!")
                    print()
                elif BookPrice % 1 == 0:
                    BookPriceList.append(int(BookPrice))
                    BookPriceEntryDone+=1
                    CurrentBookNumber+=1
                else:
                    BookPriceList.append(float(BookPrice))
                    BookPriceEntryDone+=1
                    CurrentBookNumber+=1

        
    
    clear_console()
    CurrentBookNumber=0
    print("Your Cart:")
    while CurrentBookNumber!=BookAmount:
        print("  "+BookList[CurrentBookNumber]+" - "+str(BookPriceList[CurrentBookNumber])+"$")
        CurrentBookNumber+=1
    print("Your Total is: "+str(sum(BookPriceList))+"$")

    exit(0)

main()