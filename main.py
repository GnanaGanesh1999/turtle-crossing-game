import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing ")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.display_level()

screen.listen()
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_forward, "Up")

game_is_on = True
start_time = time.time()
scoreboard.increase_level()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    time_diff = int(time.time() - start_time)

    if scoreboard.current_level == 1:
        time_diff -= 6

    scoreboard.display_timer(time_diff)
    if not player.step_counted:
        scoreboard.increase_score(1)
        player.step_counted = True

    for car in car_manager.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.display_game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.display_center_text(f"Level {scoreboard.current_level} Cleared!", sleep_time=3)

        time_bonus = 0
        if time_diff < 10:
            time_bonus = 100
        elif time_diff < 20:
            time_bonus = 75
        elif time_diff < 30:
            time_bonus = 50

        level_bonus = scoreboard.current_level * 25

        scoreboard.display_bonus_score(time_bonus, level_bonus)
        scoreboard.increase_level()
        start_time = time.time()

screen.exitonclick()
