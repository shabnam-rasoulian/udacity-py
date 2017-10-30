import turtle

def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("red")
    shabnam = turtle.Turtle()
    shabnam.color("white")
    shabnam.speed(2)
    shabnam.shape("square")
    for i in range(4):
        shabnam.forward(100)
        shabnam.right(90)

    screen.exitonclick()

draw_square()

