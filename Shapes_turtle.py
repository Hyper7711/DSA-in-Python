import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Basic Shapes with Turtle")

# Create a turtle object
pen = turtle.Turtle()

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        pen.forward(side_length)
        pen.right(120)

# Function to draw a circle
def draw_circle(radius):
    pen.circle(radius)

# Function to draw a polygon with n sides
def draw_polygon(sides, side_length):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(side_length)
        pen.right(angle)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Function to draw an oval
def draw_oval(radius):
    for _ in range(2):
        pen.circle(radius,90)
        pen.circle(radius//2,90)

# Function to draw a semi-circle
def draw_semi_circle(radius):
    pen.circle(radius, 180)

# Function to draw a spiral
def draw_spiral(length, angle):
    for i in range(length):
        pen.forward(i)
        pen.right(angle)

# Draw the shapes
pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_square(100)

pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_rectangle(150, 100)

pen.penup()
pen.goto(200, 0)
pen.pendown()
draw_triangle(100)

pen.penup()
pen.goto(-150, -200)
pen.pendown()
draw_circle(50)

pen.penup()
pen.goto(0, -200)
pen.pendown()
draw_polygon(5, 70)

pen.penup()
pen.goto(150, -200)
pen.pendown()
draw_star(100)

pen.penup()
pen.goto(0, -50)
pen.pendown()
draw_polygon(6, 70)

pen.penup()
pen.goto(-200, 150)
pen.pendown()
pen.setheading(45)  # Angle the oval
draw_oval(100)

pen.penup()
pen.goto(150, 150)
pen.pendown()
draw_semi_circle(70)

pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_spiral(100, 45)

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()