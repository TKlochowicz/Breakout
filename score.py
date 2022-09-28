from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        with open("data.txt") as self.file:
            self.high_score = int(self.file.read())
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}; High Score: {self.high_score}", align="center", font=("Courier New", 14, "normal"))

    def brick_destroyed(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as self.file:
                self.file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()


    def game_over(self):
        self.goto(0, 100)
        self.write(f"GAME OVER", align="center", font=("Courier New", 20, "normal"))