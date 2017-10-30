import turtle

def draw_square(shape):
    for i in range(4):
        shape.forward(200)
        shape.right(90)

def draw_fractal():
    screen = turtle.Screen()
    screen.bgcolor("red")
    fractal = turtle.Turtle()
    fractal.shape("arrow")
    fractal.speed(10)
    fractal.color("white")
    for i in range(36):
        draw_square(fractal)
        fractal.right(10)

    screen.exitonclick()
    
draw_fractal()
