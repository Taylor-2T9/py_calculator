import colors

class Operator:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.bg = colors.orange
        self.fg = colors.white
        self.command = ''

percent = Operator('%', 118, 0, 5, 2)
division = Operator('/', 177, 0, 5, 2)
multiplication = Operator('*', 177, 52, 5, 2)
subtraction = Operator('-', 177, 104, 5, 2)
sum = Operator('+', 177, 156, 5, 2)
equal = Operator('=', 177, 208, 5, 2)

operators = []
operators.extend([percent, division, multiplication, subtraction, sum, equal])