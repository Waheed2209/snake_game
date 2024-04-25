from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5 , stretch_wid= 0.5)
        self.speed("fastest")
        self.color("red")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)