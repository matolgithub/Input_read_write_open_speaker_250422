import time
from tkinter import *
from tkinter import  Canvas
import random

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, fill_color, outline_color, delta_x, delta_y, text_ball):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.color_ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.fill_color,
                                             outline=self.outline_color)
        self.text_ball = canvas.create_text(x1 + 29, y1 + 29, text=text_ball)

    # It is function for moving down different text/color balls
    def move_ball_down(self):
        delta_x = 0
        stop_y = 300
        delta_y = self.delta_y
        try:
            if canvas.coords(self.color_ball)[1] < stop_y:
                delta_y = self.delta_y
            elif canvas.coords(self.color_ball)[1] >= stop_y and Ball.count_move < 200:
                num_jump = -8
                delta_y = self.delta_y * num_jump
            elif canvas.coords(self.color_ball)[1] >= stop_y and Ball.count_move > 200:
                delta_y = 0
                if Ball.count_move >= 600:
                    self.canvas.delete('all')
                    self.draw_logo()
            self.canvas.move(self.color_ball, delta_x, delta_y)
            self.canvas.move(self.text_ball, delta_x, delta_y)
            Ball.count_move += 1
        except IndexError:
            self.canvas.delete('all')
        except UnboundLocalError:
            self.canvas.delete('all')
        self.canvas.after(20, self.move_ball_down)

    # It is function for draw logo with different colors
    def draw_logo(self):
        second_canvas = Canvas(canvas, width=400, height=400, bg='black')
        x1, y1, x2, y2 = 100, 100, 200, 200
        second_canvas.pack()
        count = 0
        while count <= 10:
            color_list = ['#4BD0A0', '#0066FF', '#5D00F5', '#EB236B', 'white', 'grey', 'green', 'pink', 'yellow', 'blue']
            dif_color_1 = random.choice(color_list)
            ball_5 = Ball(second_canvas, x1, y1, x2, y2, dif_color_1, dif_color_1, 0, 0, '')
            color_list.remove(dif_color_1)
            dif_color_2 = random.choice(color_list)
            ball_6 = Ball(second_canvas, x1 + 110, y1, x2 + 110, y2, dif_color_2, dif_color_2, 0, 0, '')
            color_list.remove(dif_color_2)
            dif_color_3 = random.choice(color_list)
            ball_7 = Ball(second_canvas, x1, y1 + 110, x2, y2 + 110, dif_color_3, dif_color_3, 0, 0, '')
            color_list.remove(dif_color_3)
            dif_color_4 = random.choice(color_list)
            ball_8 = Ball(second_canvas, x1 + 110, y1 + 110, x2 + 110, y2 + 110, dif_color_4, dif_color_4, 0, 0, '')
            color_list.remove(dif_color_4)
            ball_9 = Ball(second_canvas, x1 + 55, y1 + 55, x2 + 55, y2 + 55, 'black', 'black', 0, 0, '')
            dif_color_5 = random.choice(color_list)
            text_logo = second_canvas.create_text(x1 + 100, y1 - 50, text='NETOLOGY', fill=dif_color_5)
            second_canvas.update()
            color_list.extend([dif_color_1, dif_color_2, dif_color_3, dif_color_4])
            time.sleep(0.5)
            count += 1

# initialize window and canvas
window = Tk()
window['bg'] = 'black'
window.title("LOGO 'Netology' - color balls!")
window.resizable(False,False)
canvas = Canvas(window, width=400, height=400, bg='black')
canvas.pack()
btn_1 = Button(window, text='Click the Button to Exit', command=quit)
btn_1.pack(padx=10, pady=10, side=RIGHT)

# create ball objects and animate them
x1, y1, x2, y2, delta_x, delta_y = 80, 30, 139, 89, 0, 10
Ball.count_move = 0
ball_1 = Ball(canvas, x1, y1, x2, y2, '#4BD0A0', '#4BD0A0', delta_x, delta_y + 1, 'NE')
ball_2 = Ball(canvas, x1 + 60, y1, x2 + 60, y2, '#0066FF', '#0066FF', delta_x, delta_y + 2 , 'TO')
ball_3 = Ball(canvas, x1 + 120, y1, x2 + 120, y2, '#5D00F5', '#5D00F5', delta_x, delta_y + 1, 'LO')
ball_4 = Ball(canvas, x1 + 180, y1, x2 + 180, y2, '#EB236B', '#EB236B', delta_x, delta_y + 2, 'GY')
ball_1.move_ball_down()
ball_2.move_ball_down()
ball_3.move_ball_down()
ball_4.move_ball_down()

window.mainloop()
