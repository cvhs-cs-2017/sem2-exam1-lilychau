"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""
print("Enter your favorite number")
n = int(input())
c = 0
N = n
while N >= 100:
    n += 5
    c += 1
    
print(N)





"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
#if you laughed then i should get E.C. for jokes
n = int(input("Give me a number under 100. 'Even' if the 'Odds' aren't in your favor: "))

def EvenOddFunc(n):
    if n%2 == 0 :
        n = n * 3
    elif n%2 != 0 :
        n = n * 2
    else:
        print("Okay, i asked for a number...")

print(EvenOddFunc(n))
