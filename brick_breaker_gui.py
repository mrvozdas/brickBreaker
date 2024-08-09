import tkinter as tk
import sys
from os import path
from PIL import Image, ImageTk


class BrickBreaker(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=600, background='black', highlightthickness=0)
        self.paddle_position = [(250, 500)]

        self.load_assets()
        self.create_object()

    def load_assets(self):
        try:
            bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
            path_to_brick = path.join(bundle_dir, "assets", "brick.png")
            path_to_paddle = path.join(bundle_dir, "assets", "paddle.png")
            path_to_ball = path.join(bundle_dir, "assets", "ball.png")

            self.brick_image = Image.open(path_to_brick)
            self.brick = ImageTk.PhotoImage(self.brick_image)

            self.paddle_image = Image.open(path_to_paddle)
            self.paddle = ImageTk.PhotoImage(self.paddle_image)

            self.ball_image = Image.open(path_to_ball)
            self.ball = ImageTk.PhotoImage(self.ball_image)

        except IOError as e:
            print(e)
            root.destroy()

    def create_object(self):
        self.create_image(50, 50, image=self.brick, tag="brick")
        self.create_image(self.paddle_position[0][0], self.paddle_position[0][1], image=self.paddle, tag="paddle")
        self.create_image(200, 200, image=self.ball, tag='ball')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Brick Breaker')
    root.resizable(False, False)

    board = BrickBreaker()
    board.pack()

    root.mainloop()
