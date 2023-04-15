import colors
from tkinter import *
from tkinter import ttk
from buttons import element_button, action_button
from numbers import numbers
from operators import operators
from special_chars import special_chars

window = Tk()
window.title('Calculadora')
window.geometry('235x315')
window.configure(bg=colors.white)

# Frames #
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)
screen_frame = Frame(window, width=300, height=56,bg=colors.dark_gray, pady=0, padx=0, relief="flat")
screen_frame.grid(row=1, column=0, sticky=NW)
buttons_frame = Frame(window, width=300, height=340,bg=colors.dark_gray, pady=0, padx=0, relief="flat")
buttons_frame.grid(row=2, column=0, sticky=NW)

expression = ""
text = StringVar()

def get_value(event):
    global expression
    expression = expression + str(event)
    text.set(expression)
def calc():
    global expression
    result = str(eval(expression))
    text.set(result)
    expression = result
def clean_screen():
    global expression
    text.set("")
    expression = ""


for number in numbers:
    number.command = get_value
    element_button(number, buttons_frame)
for operator in operators:
    if(operator.label == '='):
        operator.command = calc
        action_button(operator, buttons_frame)
    else:
        operator.command = get_value
        element_button(operator, buttons_frame)
for special_char in special_chars:
    if(special_char.label == '.'):
        special_char.command = get_value
        element_button(special_char, buttons_frame)
    else:
        special_char.command = clean_screen
        action_button(special_char, buttons_frame)

app_scream = Label(screen_frame, textvariable=text, width=16, height=2, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg=colors.matte_blue, fg=colors.white)
app_scream.place(x=0, y=0)

window.mainloop()
