from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.goto(0, 0)
        self.penup()
        self.x_rate = 10
        self.y_rate = 10
        self.move_speed = 0.08

    def move(self):
        x_cor = self.xcor() + self.x_rate
        y_cor = self.ycor() + self.y_rate
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_rate *= -1

    def bounce_x(self):
        self.x_rate *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()
