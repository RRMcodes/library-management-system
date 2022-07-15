# datetime module is imported
import datetime

#this function converts string inputted by user to date

def date(a):

    l = a.split("/") 
    x = int(l[0])
    y = int(l[1])
    z = int(l[2])
    date = datetime.datetime(x,y,z)
    return date # converted date is returned

