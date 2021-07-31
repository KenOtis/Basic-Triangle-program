def Stars():
    print("Star Triangle:")
    a="*"
    n=5
    for i in range (0,n):            ##handles the number of rows 
        for j in range(0,i+1):       ##handles the number of columns
            print (a,end="")         ##prints the stars 
        print ("\r")                 ##ending each line after the row 
Stars()



def CountingTriangle():
    print ("\nCountring Triangle:")
    n=1                              ##Starting with this number 
    times=5                          ##How many rows
    for i in range (0,times):        ##loop to handle the rows 
        n=1                          ##reassign the variable in this loop 
        for j in range (0,i+1):
            print (n,end="")         ##printing the numbers
            n=n+1                    ##Changing the number to add as counting goes up
        print ("\r")
CountingTriangle()

def ReverseCountingTriangle():
    print ("\nReverse counting Triangle:")
    n=5                              ##Starting with this number 
    times=5                          ##How many rows
    for i in range (0,times):        ##loop to handle the rows 
        n=5                          ##reassign the variable in this loop 
        for j in range (0,i+1):
            print (n,end="")         ##printing the numbers
            n=n-1                    ##Changing the number to subtracting as counting goes up
        print ("\r")
ReverseCountingTriangle()