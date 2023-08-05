from math import ceil

abs

syms = ['█', ' ', '░', '▒', '▓', '╣', '╠']
'''
▒▓=syms[3]+syms[4]
'''


class Field:

    def __init__(self, width, height, field_sym=syms[1] * 2):
        self.width = width
        self.height = height
        self.field = []
        self.field_sym = field_sym
        h = 0

        while h < height:
            h += 1
            w = 0
            w_list = []
            while w < width:
                w += 1
                w_list.append(self.field_sym)

            self.field.append(w_list)

    def draw(self):
        for x in self.field:
            for y in x:
                print(y, end='')
            print()


class Point:

    def __init__(self, x, y, f: Field, sym=syms[0] * 2):
        self.x = x
        self.y = y
        self.sym = sym
        self.f = f

    def draw(self):
        self.f.field[self.y][self.x] = self.sym


# Lines
class HorizontalLine:

    def __init__(self, left_x, right_x, y, f: Field, sym=syms[0] * 2):
        self.left_x = left_x
        self.right_x = right_x
        self.y = y
        self.sym = sym
        self.f = f

    def draw(self):
        for x in range(self.left_x, self.right_x + 1):
            p = Point(x, self.y, self.f, self.sym, )
            p.draw()


class VerticalLine:

    def __init__(self, x, up_y, down_y, f: Field, sym=syms[0] * 2):
        self.x = x
        self.up_y = up_y
        self.down_y = down_y
        self.sym = sym
        self.f = f

    def draw(self):
        for y in range(self.up_y, self.down_y + 1):
            p = Point(self.x, y, self.f, self.sym)
            p.draw()

# Figures
class Rect:

    def __init__(self, x_start, y_start, x_end, y_end, f: Field, sym=syms[0] * 2):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.sym = sym
        self.f = f

    def draw(self):
        for x in range(self.x_start, self.x_end + 1):
            for y in range(self.y_start, self.y_end + 1):
                p = Point(x, y, self.f, self.sym)
                p.draw()


class Literals:

    def __init__(self, x_start, y_start, x_end, y_end, literal, f: Field, sym=syms[0] * 2):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.literal = literal
        self.f = f
        self.sym = sym

    def draw(self):
        x_start = self.x_start
        y_start = self.y_start
        x_end = self.x_end
        y_end = self.y_end
        literal = self.literal.upper()
        f = self.f
        sym = self.sym
        bg_sym=f.field_sym
        dy = y_end - y_start
        dx = x_end - x_start
        y_half_1 = y_start+ceil(dy/2)
        y_half_2 = y_start + y_half_1
        x_half_1 = x_start+ceil(dx/2)
        x_half_2 = x_start + x_half_1
        y_mid = y_start + ceil(dy / 2)
        x_mid = x_start + ceil(dx / 2)
        # up
        l_up = HorizontalLine(x_start, x_end, y_start, f, sym)
        l_up_half_1 = HorizontalLine(x_start, x_half_1, y_start, f, sym)
        l_up_half_2 = HorizontalLine(x_half_2, x_end, y_start, f, sym)
        # mid horizontal
        l_mid_hor = HorizontalLine(x_start, x_end, y_mid, f, sym)
        l_mid_hor_half_1 = HorizontalLine(x_start, x_half_1, y_mid, f, sym)
        l_mid_hor_half_2 = HorizontalLine(x_half_2, x_end, y_mid, f, sym)
        # down
        l_down = HorizontalLine(x_start, x_end, y_end, f, sym)
        l_down_half_1 = HorizontalLine(x_start, x_half_1, y_end, f, sym)
        l_down_half_2 = HorizontalLine(x_half_2, x_end, y_end, f, sym)
        # left
        l_left = VerticalLine(x_start, y_start, y_end, f, sym)
        l_left_half_1 = VerticalLine(x_start, y_start, y_half_1, f, sym)
        l_left_half_2 = VerticalLine(x_start, y_half_2, y_end, f, sym)
        # right
        l_right = VerticalLine(x_end, y_start, y_end, f, sym)
        l_right_half_1 = VerticalLine(x_end, y_start, y_half_1, f, sym)
        l_right_half_2 = VerticalLine(x_end, y_half_2, y_end, f, sym)
        # mid vertical
        l_mid_vert = VerticalLine(x_mid, y_start, y_end, f, sym)
        l_mid_vert_half_1 = VerticalLine(x_mid, y_start, y_half_1, f, sym)
        l_mid_vert_half_2 = VerticalLine(x_mid, y_half_2, y_end, f, sym)
        if literal == 'П':
            l_up.draw()
            l_right.draw()
            l_left.draw()
        if literal == 'Р':
            l_left.draw()
            l_up.draw()
            l_mid_hor.draw()
            l_right_half_1.draw()
        if literal == 'И':
            l_right.draw()
            l_left.draw()
            l_down.draw()
            p = Point(x_end - 1, y_end, f, bg_sym)
            p.draw()
            l_spec = VerticalLine(x_end - 2, y_start, y_end, f)
            l_spec.draw()
            p = Point(x_end - 1, y_start, f)
            p.draw()
        if literal == 'В':
            l_left.draw()
            l_right.draw()
            l_up.draw()
            l_down.draw()
            l_mid_hor.draw()
            p = Point(x_end, y_end, f, bg_sym)
            p.draw()
            p = Point(x_end, y_start, f, bg_sym)
            p.draw()
            p = Point(x_end, y_mid, f, bg_sym)
            p.draw()
        if literal == 'Е':
            l_left.draw()
            l_up.draw()
            l_down.draw()
            l_mid_hor.draw()
        if literal == 'Т':
            l_up.draw()
            l_mid_vert.draw()






