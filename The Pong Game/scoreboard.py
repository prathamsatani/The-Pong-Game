from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(pos_x, pos_y)
        self.write(arg=self.score, font=('Ariel', 50, 'bold'))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, font=('Ariel', 50, 'bold'))
