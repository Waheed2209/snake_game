from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]
        self.head.shape("circle")


    def make_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
    def move(self):

        for segs in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[segs - 1].xcor()
            y_axis = self.segments[segs - 1].ycor()
            self.segments[segs].goto(x_axis, y_axis)
        self.head.forward(MOVING_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.setpos(500, 500)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]
        self.head.shape("circle")