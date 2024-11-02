import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Basic Shapes with Turtle")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)  # Adjust speed for a smoother drawing experience


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
def draw_oval(width, height):
    for _ in range(2):
        pen.circle(width, 90)
        pen.circle(height, 90)


# Function to draw a semi-circle
def draw_semi_circle(radius):
    pen.circle(radius, 180)


# Function to draw a spiral
def draw_spiral(length, angle):
    for i in range(length):
        pen.forward(i * 2)
        pen.right(angle)


# Arrange shapes in a grid pattern for better organization


# Draw square
pen.penup()
pen.goto(-300, 150)
pen.pendown()
draw_square(100)

# Draw rectangle
pen.penup()
pen.goto(-150, 150)
pen.pendown()
draw_rectangle(120, 70)

# Draw triangle
pen.penup()
pen.goto(50, 150)
pen.pendown()
draw_triangle(100)

# Draw circle
pen.penup()
pen.goto(200, 150)
pen.pendown()
draw_circle(50)

# Draw pentagon
pen.penup()
pen.goto(-250, -50)
pen.pendown()
draw_polygon(5, 70)

# Draw hexagon
pen.penup()
pen.goto(-50, -50)
pen.pendown()
draw_polygon(6, 60)

# Draw star
pen.penup()
pen.goto(150, -50)
pen.pendown()
draw_star(100)

# Draw oval
pen.penup()
pen.goto(-200, -250)
pen.setheading(0)  # Reset heading before drawing oval
pen.pendown()
draw_oval(50, 100)

# Draw semi-circle
pen.penup()
pen.goto(0, -250)
pen.setheading(0)
pen.pendown()
draw_semi_circle(70)

# Draw spiral
pen.penup()
pen.goto(200, -250)
pen.setheading(0)
pen.pendown()
draw_spiral(50, 45)

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
