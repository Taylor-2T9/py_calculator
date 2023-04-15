import colors

class Special_Char:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.bg = colors.light_gray
        self.fg = colors.dark_gray
        self.command = ''

dot = Special_Char('.', 118, 208, 5, 2)
clean = Special_Char('C', 0, 0, 11, 2)

special_chars = []
special_chars.extend([dot, clean])