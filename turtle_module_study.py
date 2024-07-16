import random
import turtle  # this is how we use it
# if we use 'import Turtle form turtle' command, then we do not need to put turtle. in front of every method we use

colors = ['red', 'yellow', 'blue', 'purple']
tortoise = turtle.Turtle()
# we need to create an object to run methods on, turtle. is the module and Turtle() is the class
# we can have multiple turtle objects too
tortoise.color('red')
tortoise.pensize(5)
tortoise.shape('turtle')  # there are a few diff shape options
# these are basic properties we can give the turtle object

# screen
wn = turtle.Screen()
wn.title("Turtle for Beginners!")  # sets title for the separate turtle window
wn.bgcolor("white")


tortoise.speed(10) # we can control pen drawing speed, 1 is approximately the slowest
tortoise.forward(100)  # inside the number is pixels we want the object to move in particular direction
tortoise.left(100)
tortoise.penup()
# this lifts the pen up hence line is not drawn when turtle moves
tortoise.color('green') # we can change attributes any time
tortoise.backward(90)
tortoise.right(90)
tortoise.pendown() # this puts pen back down
# these are basic turtle object movements

# fill in shape with color
tortoise.begin_fill()
tortoise.circle(50)
tortoise.end_fill()

# using a for loop to create a square
for i in range(4):
    tortoise.forward(100)
    tortoise.right(90)
# we use setpos to set position of the object, format is cartisian plane (x/y axis)
for j in range(5):  # this will create 5 shapes
    randx = random.randint(0, 100)
    randy = random.randint(0, 100)
    tortoise.penup()
    tortoise.setpos(randx, randy)  # we have to set both x and y coordinates
    tortoise.pendown()
    tortoise.circle(50)  # we have to mention shape or it will not draw


# drawing using  our keys on screen
def up():
    tortoise.setheading(90)  # sets angle 0 - east,  90 - north, 180 - west, 270 - south
    tortoise.forward(100)


def down():
    tortoise.setheading(270)
    tortoise.forward(100)


def left():
    tortoise.setheading(180)
    tortoise.forward(100)


def right():
    tortoise.setheading(0)
    tortoise.forward(100)


def clickright(x, y):
    tortoise.color(random.choice(colors))

def clickleft(x, y):
    tortoise.stamp()  # stamps the object whenever we use this method


# turtle.method(x, y) x represents name of function we are using and y represents the keys on our keyboard we assign)
turtle.listen()  # will take our key inputs and listen for events

turtle.onscreenclick(clickright, 3) # 1 is left mouse button, 2 is middle (scroll wheel) and 3 is right
turtle.onscreenclick(clickleft, 1)
turtle.onkey(up, 'Up')  # when we press up it moves up, 'Up' can be changed into any key on the keyboard we want
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()  # we need to add this or else program will close immediately

# function design with turtle to let us draw on screen
def sketching(x, y):
    tortoise.ondrag(None)
    tortoise.setheading(tortoise.towards(x, y))
    tortoise.goto(x, y)
    tortoise.ondrag(sketching)

def scrollclick():
    tortoise.clear()

def main():
    turtle.listen()
    tortoise.ondrag(sketching)
    turtle.onscreenclick(scrollclick(), 2)
    wn.mainloop()


main()


