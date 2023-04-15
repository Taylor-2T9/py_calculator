from tkinter import *

def action_button(item, frame):
    button = Button(frame, command= lambda: item.command(), text=item.label, width=item.width, height=item.height, bg=item.bg, fg=item.fg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    button.place(x=item.x, y=item.y)
    return button
def element_button(item, frame):
    button = Button(frame, command= lambda: item.command(item.label), text=item.label, width=item.width, height=item.height, bg=item.bg, fg=item.fg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    button.place(x=item.x, y=item.y)
    return button