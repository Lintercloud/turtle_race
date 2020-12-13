from turtle import *
import random

screen = Screen()

screen.setup(height=400, width = 500)
user_bet = screen,textinput("Make your bet", "Which color would win the race? make your bet")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle_move in all_turtle:
        move_distance = random.randint(0, 10)
        turtle_move.forward(move_distance)
        if turtle_move.xcor() > 235:
            if user_bet == turtle_move.pencolor():
                print(f"you win the game, the winner is {turtle_move.pencolor()}")
            else:
                print(f"you lose the game, the winner is {turtle_move.pencolor()}")
            is_race_on = False

screen.exitonclick()