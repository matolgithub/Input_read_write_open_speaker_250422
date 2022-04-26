from tkinter import *
from tkinter import Canvas
import math
import random


def move():
    global angle
    x1, y1, x2, y2 = 200, 150, 300, 250
    dif_color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    ball_1 = canvas.create_oval(x1, y1, x2, y2, fill=dif_color, outline='black')
    txt_1 = canvas.create_text(x1 + 200, y1 - 120, text='NETOLOGY', fill=dif_color)
    line_1 = canvas.create_line(x1 - 120, y1 + 150, x1 - 120, y1 + 200, fill=dif_color)
    rect_1 = canvas.create_rectangle(x1 + 180, y1 + 180, x2 + 120, y2 + 120, fill=dif_color)
    canvas.create_oval(x1, y1 + 50, x2, y2 + 50, fill='black', outline='black')
    delta_x = ((x2 - x1) * math.sin(angle)) / 2
    delta_y = ((x2 - x1) / 2) * (((4 * ((math.sin(angle / 2))) ** 2) - ((math.sin(angle)) ** 2)) ** 0.5)
    canvas.move(ball_1, delta_x, delta_y)
    canvas.move(txt_1, delta_x, delta_y)
    canvas.move(line_1, delta_x, delta_y)
    canvas.move(rect_1, delta_x, delta_y)
    angle += 1
    if angle <= 200:
        print(angle, x1, y1, x2, y2, canvas.coords(ball_1)[2], delta_x, delta_y)
        canvas.after(10, move)
    else:
        canvas.delete('all')
        canvas.create_oval(x1 - 50, y1, x2 - 50, y2, fill='#EB236B', outline='#EB236B')
        canvas.create_oval(x1 + 50, y1, x2 + 50, y2, fill='#4BD0A0', outline='#4BD0A0')
        canvas.create_oval(x1 - 50, y1 + 100, x2 - 50, y2 + 100, fill='#5D00F5', outline='#5D00F5')
        canvas.create_oval(x1 + 50, y1 + 100, x2 + 50, y2 + 100, fill='#0066FF', outline='#0066FF')
        canvas.create_oval(x1, y1 + 50, x2, y2 + 50, fill='black', outline='black')

window = Tk()
window['bg'] = 'black'
btn_1 = Button(window, text='Quit', padx=20, pady=5, command=quit)
canvas = Canvas(window, width=500, height= 500, bg='black')
canvas.pack(expand=True, fill='both')
btn_1.pack(padx=5, pady=10, side='right')
angle = 0
move()
window.mainloop()