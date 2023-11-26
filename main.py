from turtle import Screen
import time
import player
import carmanager
import scoreboard

screen = Screen()
screen.setup(width=800, height=500)
screen.title("Charoy Zand St.")
screen.tracer(0)

player = player.Player()
cars = carmanager.CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car) < 40:
            if scoreboard.lives > 1:
                scoreboard.loose_life()
                player.rest_position()
            else:
                print("collision")
                game_is_on = False
                scoreboard.game_over()
        if car.xcor() < - 450:
            cars.all_cars.remove(car)

    if player.at_finish():
        scoreboard.level += 1
        player.rest_position()
        cars.increase_speed()
        scoreboard.update_scoreboard()

screen.exitonclick()
