import colors

class Number:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.bg = colors.light_gray
        self.fg = colors.dark_gray
        self.command = ''

one = Number('1', 0, 156, 5, 2)
two = Number('2', 59, 156, 5, 2)
three = Number('3', 118, 156, 5, 2)
four = Number('4', 0, 104, 5, 2)
five = Number('5', 59, 104, 5, 2)
six = Number('6', 118, 104, 5, 2)
seven = Number('7', 0, 52, 5, 2)
eight = Number('8', 59, 52, 5, 2)
nine = Number('9', 118, 52, 5, 2)
zero = Number('0', 0, 208, 11, 2)

numbers = []
numbers.extend([one, two, three, four, five, six, seven, eight, nine, zero])