import turtle
import time
import random

WIDTH = 500
HEIGHT = 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

def move():
    x = snake.xcor()
    y = snake.ycor()
    if segments:
        segments[0].goto(x, y)

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if snake.distance(food) < 20:
        food.goto(random.randint(-WIDTH//2, WIDTH//2), random.randint(-HEIGHT//2, HEIGHT//2))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    snake.forward(20)

    if snake.xcor() > WIDTH//2 or snake.xcor() < -WIDTH//2 or snake.ycor() > HEIGHT//2 or snake.ycor() < -HEIGHT//2:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

screen.listen()
screen.onkeypress(lambda: snake.setheading(90), "Up")
screen.onkeypress(lambda: snake.setheading(270), "Down")
screen.onkeypress(lambda: snake.setheading(0), "Right")
screen.onkeypress(lambda: snake.setheading(180), "Left")

while True:
    screen.update()
    move()
    time.sleep(0.1)

screen.mainloop()
