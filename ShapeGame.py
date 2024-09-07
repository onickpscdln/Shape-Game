import turtle
import random
import time

# Set up the screen
window = turtle.Screen()
window.title("Shape Game")
window.bgcolor("white")
window.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("square")
player.color("pink")
player.speed(0)
player.penup()
player.goto(0, -250)

# Create the shapes
shapes = []
shape_colors = ["red", "green", "purple", "orange"]

for _ in range(4):
    shape = turtle.Turtle()
    shape.shape("triangle")
    shape.color(random.choice(shape_colors))
    shape.speed(0)
    shape.penup()
    x = random.randint(-280, 280)
    y = random.randint(100, 250)
    shape.goto(x, y)
    shapes.append(shape)

# Create the scoreboard
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= 20
    if x < -280:
        x = -280
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += 20
    if x > 280:
        x = 280
    player.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Function to check for collisions
def is_collision(shape, player):
    distance = shape.distance(player)
    return distance < 20

# Game over function
def game_over():
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
    time.sleep(2)
    window.bye()

# Main game loop
while True:
    window.update()

    for shape in shapes:
        shape.sety(shape.ycor() - 10)

        if shape.ycor() < -280:
            shape.color(random.choice(shape_colors))
            shape.goto(random.randint(-280, 280), random.randint(100, 250))

        if is_collision(shape, player):
            game_over()

    score += 10
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
