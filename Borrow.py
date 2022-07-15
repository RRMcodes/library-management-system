# Python modules are imported
import Date
import datetime

# Function borrow is defines
def Borrow():

# global variables are declared
    transaction = "borrowed"
    l = []
    count = 0
    stop = False
    d = {}

 # file books.txt is opened in reading mode and its lines are read 
    file1 = open("books.txt", "r")
    line1 = file1.readlines() 
    file1.close()

# user inputted name is converted into lowercase
    name = input("Enter your full name: ").lower() 
    print("\n")
    
    print("All the books you borrow are property of this library and should be returned within 10 days after being borrowed.\n")
    print("Following are the list of available books: \n ")

# all the available books are displayed
    for e in line1:
        l = e.split(",")
        
        if int(l[2]) > 0:
            count = count + 1
            print(count,l[0],"by",l[1],"\n")
            

    while stop == False:

        # book name is inputted
        book = input("Enter the name of book you want to borrow: ")

# this part validates the book name
        for e in line1:
            l = e.split(",")

            if l[0].lower() == book.lower():
                valid = True
                break
            else:
                valid = False

        if valid == True:

            # if book name is valid, data from transactionDetails file is read
            transactionFile = open("transactionDetails.txt","r")
            lines = transactionFile.readlines()
            transactionFile.close()

            borrowCount = 0
            returnCount = 0
        
            for each in lines:
                L = each.split(",")
        
                # previous borrow record is searched 
                if L[0] == "borrowed" and L[1] == name :
                                
                    for e in L:

                        if book.lower() == e.lower():
                            borrowedDate = L[2]
                            borrowCount = borrowCount + 1
                        
                        
                # previous return record is checked
                if L[0] == "returned" and L[1] == name :

                    for e in L:

                        if book.lower() == e.lower() :
                            returnCount = returnCount + 1
                       
            # if already  borrowed error meaasge is displayed
            if borrowCount > returnCount :
                print("you have already borrowed this book on " + borrowedDate + "\n")
                    
            else:
                # if no book is selected, current book is selected 
                if len(d) == 0:
                    d[book] = 1

                # if a book is already selected    
                else:
                    
                    # checks if current book is already selected
                    selected = False
                    for key in d:
                        if book.lower() == key.lower():
                            selected = True

                    # if current book is already selected, error message is displayed
                    if selected == True:
                        print("you have already selected this book \n")

                    # if current book is not selected, it is now selected    
                    else:
                        d[book] = 1

                # if user wants to add more books, loop continues, else the loop will stop            
                b = input("Do you want to borrow any other books? ( yes / no ) : ")
                print("\n")
                
                if b.lower() == "no":
                    stop = True
        # if the user enters invalid book name, error messsage is displayed
        else:
            print("Please enter correct book name! \n")

    x = False
    
    while x == False:

        # checks if date enter ny the user is valid
        try:
            borrowedDate = input("Enter borrowed date(yyyy/mm/dd): ")
            specifiedDate = Date.date(borrowedDate) + datetime.timedelta(days=10)
            l = str(specifiedDate)
            l = l.split()
            specifiedDate = l[0]
            specifiedDate = specifiedDate.split("-")
            specifiedDate = "/".join(specifiedDate)
            x = True

        # if date is invalid, exception is handled and error message is displayed
        except:
            print("invalid date! please enter again \n")
            
    transaction = transaction + "," + name + "," + borrowedDate
    
    # displaying 10 days return policy
    agree = input("\nall the book(s) borrowed today should be returned within " + specifiedDate + " ,if not returned on specified date, you will be charged 5% more each day. Do you agree?( yes / no): ")
    print("\n")

    # if the user agrees with policy display the book details and borrow costs
    if agree == "yes":
        
        text = ""
        text = text + "\n\nborrowed on: " + borrowedDate + "\n"
        text = text + "borrowed by: " + name + "\n"
        text = text + "return by: " + specifiedDate + "\n\n"  
        text = text + "\t\t\t\tBooks borrowed: \n\n"
        text = text + ("-"*85) + "\nS.N\tBook name\t\t\tAuthor\t\t\tcost\n" + ("-"*85) + "\n\n"
        
        c = 0
        total = 0.0
        
        for e in line1:
            l = e.split(",")

            for key in d:
                
                if key.lower() == l[0].lower():
                    c = c + d[key]
                    cost = l[3][1:-1]
                    
                    if len(key) > 14:
                        text = text + str(c) + "\t" + l[0] + "\t\t" + l[1] + "\t\t$" + str(cost) + "\n"
                        
                    else:
                        text = text + str(c) + "\t" + l[0] + "\t\t\t" + l[1] + "\t\t$" + str(cost) + "\n"
                        
                    total = total + d[key] * float(cost)
                    transaction = transaction + "," + l[0]
                    
        transaction = transaction + "," + "$" + str(total) + "\n"
        
        text = text + "\n" + "-"*85 + "\n"
        text = text + "\t\t\t\t\t\t\t\tTotal Cost = $" + str(total)
        text = text + "\n" + "="*85 + "\n"

        print(text)

        # confirm the borrowing 
        confirm = input("do you confirm to borrow ? ( yes/no ): ")

        # if the user confirms to borrow
        if confirm == "yes":

            # stock file is modified
            file2 = open("books.txt","w")

            for e in line1:
                l = e.split(",")

                for key in d:
                    if key.lower() == l[0].lower():
                        l[2] = str(int(l[2]) - d[key])
                        
                l = ",".join(l)
                file2.write(l)
                
            file2.close()

            filename = "borrowed by " + name + ".txt"

            # borrow note is generated
            file3 = open(filename,"a")
            file3.write(text)
            file3.close()

            # transaction detail is recorded
            file4 = open("transactionDetails.txt","a")
            file4.write(transaction)
            file4.close()

            print(c,"book(s) confirmed.")
            print("\n")
            print("Thank you for borrowing book(s)")
        
    
