from turtle import Turtle
from random import choice
import time

FONT = ("Courier", 24, "normal")
GAME_OVER_TEXT = ["GAME OVER", "CRASHED", "WHOOPS! HURT"]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.timer_turtle = Turtle()
        self.timer_turtle.penup()
        self.timer_turtle.hideturtle()
        self.timer_turtle.goto(-270, -290)
        self.current_level = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")

    def display_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write("Level : " + str(self.current_level), align="center", font=FONT)
        self.goto(180, 250)
        self.write("Score : " + str(self.score), align="center", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.timer_turtle.clear()
        self.display_center_text(f"Get Ready for Level {self.current_level}")
        self.display_center_text(f"3", sleep_time=1)
        self.display_center_text(f"2", sleep_time=1)
        self.display_center_text(f"1", sleep_time=1)
        self.display_center_text(f"Go!", sleep_time=1)
        self.display_level()

    def display_center_text(self, text, sleep_time=2):
        self.goto(0, 0)
        self.clear()
        self.write(text, align="center", font=FONT)
        time.sleep(sleep_time)

    def display_game_over(self):
        self.display_center_text(choice(GAME_OVER_TEXT))
        self.display_center_text(f"You Scored {self.score}!", sleep_time=10)

    def increase_score(self, score):
        self.score += score
        self.display_level()

    def display_bonus_score(self, time_bonus, level_bonus):
        if time_bonus > 0:
            self.increase_score(time_bonus)
            self.display_center_text(f"Time Bonus : +{time_bonus}", sleep_time=1)
        self.increase_score(level_bonus)
        self.display_center_text(f"Level Bonus : +{level_bonus}", sleep_time=1)
        self.display_center_text(f"Total Score : {self.score}")

    def display_timer(self, level_time):
        self.timer_turtle.clear()
        self.timer_turtle.write(f"TIme : {level_time}", align="center")
