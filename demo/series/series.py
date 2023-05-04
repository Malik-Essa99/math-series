def fibonacci(n):
    ''' This function takes a number (n) and returns the fibonacci for this number
    '''

    if type(n) != int:
        return("The input is not an integer!")
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # pass
    
def lucas(n):
    ''' This function takes a number (n) and returns the lucas number for this number'''
    if type(n) != int:
        return("The input is not an integer!")
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    # pass

def sum_series(n,num1=0,num2=1):
    ''' This function takes 1 required (n) and 2 optional (num1,num2) parameters,
    if no optional numbers were passed with the function it returns the default sum (fibonacci) 
    if specified it makes the optional numbers as base case in the function and sums the numbers to n
    '''
    if type(n) != int:
        return("The input is not an integer!")
    if num1 == 0 and num2 == 1:
        return fibonacci(n)
    elif num1 == 2 and num2 == 1:
        return lucas(n)
    else:
        if n == 0:
            return num1
        if n == 1:
            return num2
        else:
            return sum_series(n-1,num1,num2) + sum_series(n-2,num1,num2)
    # pass

def printHi():
    print("hi")
    
printHi()