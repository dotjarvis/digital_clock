import datetime
from tkinter import *

# define colors
color1 = '#3d3d3d'  # black
color2 = '#21c25c'  # greenish

root = Tk()
root.title('')
root.geometry('350x180')
root.resizable(width=False, height=False)
root.configure(background=color1)


def clock():
    date_time = datetime.datetime.now()
    time = date_time.strftime('%H:%M:%S')
    weekday = date_time.strftime('%A')
    day = date_time.day
    month = date_time.strftime('%b')
    year = date_time.strftime('%Y')
    label1.config(text=time)
    label1.after(200, clock)

    label2.config(text=f'{weekday} {day} {month} {year}')


label1 = Label(root, font='Arial 63', bg=color1, fg=color2)
label1.grid(row=0, column=0)

label2 = Label(root, font='Arial 20', bg=color1, fg=color2)
label2.grid(row=1, column=0)

clock()
root.mainloop()
