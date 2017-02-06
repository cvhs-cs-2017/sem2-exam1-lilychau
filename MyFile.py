"""Adds 10 to the parameter n and returns the result"""
n = int(input("Enter a number: "))

def AddTen(n):
    a = n + 10
    return a

print(AddTen(n))

"""DrawRectangle(Anyturtle, l, w):  Self Explanitory"""

import turtle
Anyturtle = turtle.Turtle()
l=30
w=60
def DrawRectange(Anyturtle, l, w):
    for i in range(2):
        Anyturtle.forward(l)
        Anyturtle.right(90)
        Anyturtle.forward(w)
        Anyturtle.right(90)

DrawRectange(Anyturtle, l, w)

input()

""" DrawPoly(Anyturtle, n):  Will draw a regular polygon with 'n' sides of"""
#i chose a square polygon
n = 4
def DrawPoly(Anyturtle, n):
    for i in range(n):
        Anyturtle.forward(40)
        Anyturtle.right(90)

DrawPoly(Anyturtle, 4)
input()
