from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    def move_up(self):
        if self.ycor() < 240:
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)

    def move_down(self):
        if self.ycor() > -240:
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)
