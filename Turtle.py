"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
lily = turtle.Turtle()

n = int(input("Put in a number, and ill make a cube: "))
def ThreeDCubeFunc(lily, n):
    for i in range(4):
        lily.forward(n)
        lily.right(90)
    lily.left(45)
    lily.forward(n)
    lily.right(45)
    lily.forward(n)
    lily.right(135)
    lily.forward(n)
    lily.left(45)
    lily.forward(n)
    lily.left(135)
    lily.forward(n)
    lily.left(45)
    lily.forward(n)

ThreeDCubeFunc(lily, n)
input()





"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
