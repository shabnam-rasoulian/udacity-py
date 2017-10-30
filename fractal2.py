import turtle

def draw_diamond(shape):
    for i in range(4):
        shape.forward(100)
        if i % 2 == 0:
            shape.right(45)
        else:
            shape.right(180 - 45)

def draw_fractal():
    screen = turtle.Screen()
    screen.bgcolor("red")
    diamond = turtle.Turtle()
    diamond.speed(20)
    diamond.color("white")
    diamond.shape("arrow")
    for i in range(36):
        draw_diamond(diamond)
        diamond.right(10)

    screen.exitonclick()

draw_fractal()
