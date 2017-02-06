"""Define a function that will take a parameter, n, and triple it and return
the result"""
n = 8
def TripFunc(n):
    a = n * 3
    return a

print(TripFunc(n))
#use the while function 




"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """

n = int(input("Give me your favorite number, and ill triple it: "))

print(TripFunc(n))
