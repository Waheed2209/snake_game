from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.scoreboard_tracker()

    def scoreboard_tracker(self):
        self.write(f"score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_end(self):
        self.goto(0,0)
        self.write("GAME_OVER", align="center", font=("Arial", 24, "normal"))

    def adding_score(self):
        self.clear()
        self.score += 1
        self.scoreboard_tracker()





