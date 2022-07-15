# python modules are imported
import Date
import datetime
import os

# Function Return is defined
def Return():

    # global variables are declared
    transaction = "returned"
    l = []
    count = 0
    stop = False
    d = {}
    d2 = {}
    borrowedDate = ""
    totalFine = 0.0
    finedDays = 0

    # file books.txt is opened and its data is read
    file1 = open("books.txt", "r")
    line1 = file1.readlines()
    file1.close()

    # name is inputted and converted into lowercase
    name = input("Enter your full name: ").lower()
    
    x = False
    
    while x == False:

        # checks if date enter ny the user is valid
        try:
            returnedDate = input("Enter return date: ")
            rd = Date.date(returnedDate)
            print("\n")
            x = True

        # if date is invalid, exception is handled and error message is displayed    
        except:
            print("invalid date! please enter again \n")
            
    transaction = transaction + "," + name + "," + returnedDate
    filename = "borrowed by " + name + ".txt"

    # if the user's borrow nonte does not exsts, error message is displayed
    if os.path.isfile(filename) == False:
        print("Sorry, you haven't borrowed any books")

    # if the user's borrow note is found, it is opened and read
    else:
        file2 = open(filename,"r")
        line2 = file2.read()
        print(line2)
            
        while stop == False:

            # book name is inputted
            book = input("Enter the name of book you want to return: ")

            # checks if book name is valid                
            for e in line1:
                l = e.split(",")

                if l[0].lower() == book.lower():
                    valid = True
                    break
                
                else:
                    valid = False

            # if book name is valid 
            if valid == True:
                
                borrowCount = 0
                returnCount = 0

                # transactionDetails file is opened and read
                transactionFile = open("transactionDetails.txt","r")
                lines = transactionFile.readlines()
                transactionFile.close()

                for each in lines:
                    L = each.split(",")

                    # previous borrow record is searched
                    if L[0] == "borrowed" and L[1] == name and book in each.lower():
                        bc = 0
                        
                        for e in L:
                            if book.lower() == e.lower():
                                
                                borrowedDate = L[2]
                                finedDays = Date.date(returnedDate) - Date.date(borrowedDate)
                                l3 = str(finedDays)
                                l3 = l3.split()
                                l3 = l3[0]
                                d2[book] = int(l3)
                                bc = bc + 1
                                        
                        borrowCount = bc

                    # previous return record is searched     
                    if L[0] == "returned" and L[1] == name and book in each.lower():
                        rc = 0
                        
                        for e in L:
                            if book.lower() == e.lower() :
                                bookReturnDate = L[2]
                                rc = rc + 1
                        returnCount = rc
                                  
                # if book is borrowed              
                if borrowCount > 0:

                    # if book is not returned
                    if borrowCount > returnCount:

                        # if no book is selected, current book i selected
                        if len(d) == 0:
                            d[book] = 1

                        # if a book is already selected    
                        else:
                            
                            # checks if current book is already selected, error message is displayed
                            selected = False
                            for key in d:
                                
                                if book.lower() == key.lower():
                                    selected = True

                            if selected == True:
                                print("you have already entered the name of this book \n")

                            # if current book is not selected, it is now selected   
                            else:
                                d[book] = 1
                                    
                        # if user wants to add select books, loop continues, else the loop will stop
                        b = input("Do you want to return any other books? ( yes / no ) : ")
                        print("\n")
                        
                        if b.lower() == "no":
                            stop = True
                                    
                    else:
                        print("you have already returned this book on " + bookReturnDate + "\n" )
                    
                else:
                    print("you haven't borrowed this book \n")

            else:        
                print("please enter correct book name! \n")
                        
        finedAmount = 0.0                    
        c = 0
        total = 0.0
        n = 0
        
        text = ""
        text = text + ("\n\nborrowed on: " + borrowedDate + "\n")
        text = text + ("returned on: " + returnedDate + "\n")
        text = text + ("borrowed by: " + name + "\n\n")
        text = text + ("\t\t\t\tBooks returned: \n\n")
        text = text + ("-"*105 + "\nS.N\tBook name\t\t\tAuthor\t\t\tcost\tFined days\tFinedAmount\n" + "-"*105 + "\n\n")
        
        # book details and fined amounts are displayed
        for e in line1:
            l = e.split(",")

            for key in d:
                if key.lower() == l[0].lower():

                    c = c + d[key]
                    n = n + 1
                    l[2] = str(int(l[2]) + d[key])
                    cost = l[3][1:-1]

                    finedDays = d2[key]
                    finedDays = finedDays - 10
                    
                    if finedDays > 0 :

                        for i in range (finedDays):
                            finedAmount = float(cost) * 0.05
                            finedAmount = finedAmount + finedAmount  * 0.05

                        totalFine = round((totalFine + finedAmount),2)
                        
                    else:
                        finedDays = 0

                    if len(key) > 14:
                        text = text + str(n) + "\t" + l[0] + "\t\t" + l[1] +  "\t\t$" + str(cost) + "\t" + str(finedDays) + "\t\t$" + str(round(finedAmount,2)) + "\n\n"

                    else:
                        text = text + str(n) + "\t" + l[0] + "\t\t\t" + l[1] +  "\t\t$" + str(cost) + "\t" + str(finedDays) + "\t\t$" + str(round(finedAmount,2)) + "\n\n"
                        
                    transaction = transaction + "," + l[0]
                    
        text = text + "-"*105
        text = text + "\n\t\t\t\t\t\t\t\t\t\tTotal fine amount = $" + str(totalFine) + "\n" + "="*105
        print(text)
        print("\n")

        transaction = transaction + "," + "$" + str(totalFine) + "\n"


        # user confirmation is asked
        confirm = input("Do you confirm to return " + str(c) + " books? (yes/no) : ")

        # if user confirms to return books
        if confirm == "yes":

            # stock file is updated
            file2 = open("books.txt","w")

            for e in line1:
                l = e.split(",")

                for key in d:
                    if key.lower() == l[0].lower():
                        l[2] = str(int(l[2]) + d[key])
                        
                l = ",".join(l)
                file2.write(l)

            file2.close()

            filename = "returned by " + name + ".txt"

            # return note is generated   
            file4 = open(filename,"a")
            file4.write(text)
            file4.close()

            # transaction detail is recorded
            file5 = open("transactionDetails.txt","a")
            file5.write(transaction)
            file5.close()

            print(str(c) + " book(s) confirmed")
            print("\n")
            print("Thank you for returning the book(s)")
