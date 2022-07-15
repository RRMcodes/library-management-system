# python modules are imported
import Borrow
import Return

loop = True

while loop == True:

    # user input is asked
    print("\n")
    transaction = input("Do yo want to borrow or return book(s) ? ( Enter borrow or return):  ")
    print("\n")

    # if user wants to borrow book, borrow function from borrow module is called
    if transaction.lower() == "borrow":
        Borrow.Borrow()
        loop = False

    # if user wants to return book, return function from return module is called    
    elif transaction.lower() == "return":
        Return.Return()
        loop = False

    # if user does not enter borrow or return
    else:

        #user is asked whether to exit
        exit = input("Do you want to exit ? (yes/no): ")

        # if user types yes, exit program
        if exit == "yes":
            quit()
        # if user types no, continue loop    
        elif exit == "no":
            loop = True
            print("\n")
        
        
