import turtle

def draw_square():
    square = turtle.Turtle()
    square.shape("square")
    square.color("white")
    square.speed(2)
    for i in range(4):
        square.forward(100)
        square.right(90)

def draw_circle():
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("blue")
    circle.circle(100)

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("triangle")
    triangle.color("green")
    for i in range(3):
        triangle.forward(100)
        triangle.right(120)

def draw_art():
    screen = turtle.Screen()
    screen.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    screen.exitonclick()

draw_art()

