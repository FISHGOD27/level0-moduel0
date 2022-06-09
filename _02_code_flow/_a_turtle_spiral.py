import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    
    # Make a new turtle
    a = turtle.Turtle()
    # This code sets our shape to a turtle
    a.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    a.speed(10)
    # Set your turtle's color using .color('green')
    a.color('green')
    a.turtlesize(0.1)
        # Use a loop to repeat a the code below 50 times
    a.penup()
    a.goto(x=-100,y=0)
    a.pendown()
    for i in range(22):
        a.color(get_random_color())
        a.forward(5*i)
        a.right(360/7)
        a.width(20)
    a.penup()
    a.goto(x=120,y=0)
    a.pendown()
    for i in range(21):
        a.color(get_random_color())
        a.forward(5*i)
        a.right(360/7)
        a.width(20)
    a.penup()
    a.goto(x=-250,y=-150)
    a.pendown()
    for i in range(5):
        a.left(16.7)
        a.color(get_random_color())
        a.forward(100)
    a.left(146.5)
    for i in range(4):
        a.forward(100)
        a.color(get_random_color())
    a.forward(59)

        # Set the turtle color to a random color
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        # Turn the turtle (360/7) degrees to the right
        # Change the turtle width to 'i' (the loop variable)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

