from math import ceil, floor, factorial
from sympy import factorint, divisors


def ok_sqrt(n, lenn=10):
    n *= 10 ** lenn
    u, v = 1, n // 2
    while abs(u - v) > 10:
        u, v = v, (n // v + v) // 2

    return v


def pols_in_pols(w, h):
    # polygons in polygons
    count = 0
    for x in range(1, w + 1):
        for y in range(1, h + 1):
            _w_ = w - x + 1
            _h_ = h - y + 1
            count += _h_ * _w_
    return count


def square_equation(eq):  # d=ax^2+bx+c
    components = []
    d = ''
    a = ''
    b = ''
    c = ''
    for x in eq:
        components.append(x)
        if '=' not in components:
            d += x
        if '=' in components and '^' not in components and x != '=' and x != 'x':
            a += x
        if '=' in components and '^' in components and components.count('+') == 1 and x != '+' and x != 'x':
            b += x
        if '=' in components and '^' in components and components.count('+') == 2 and x != '+':
            c += x
    if a == '':
        a = 1
    else:
        a = int(a)
    if b == '':
        b = 1
    else:
        b = int(b)
    c = int(c) - int(d)
    # ax^2+bx+c=0
    if a != 0:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return False
        x1 = (b * (-1) + D ** .5) / (2 * a)
        x2 = (b * (-1) - D ** .5) / (2 * a)
        return x1, x2
    else:
        x = (-1) * c / b
        return x


def line_equation(eq):  # a=bx+c if num<0 ->num=-num (example: c<0  ->a=bx+-c
    a = ''
    b = ''
    c = ''
    components = []
    for x in eq:
        components.append(x)
        if '=' not in components:
            a += x
        if '=' in components and 'x' not in components:
            b += x
        if '=' in components and 'x' in components and '+' in components:
            c += x
    a = int(a)
    b = int(b[1::])
    c = int(c[1::])
    x = (a - c) / b
    return x


def is_polindrom(n):
    sr = str(n)
    l = len(sr)
    if l % 2 == 0:
        if sr[0:l] == sr[l::-1]:
            return True
        else:
            return False
    else:
        if sr[0:l] == sr[l + 1::-1]:
            return True
        else:
            return False


def is_num_prime(n):
    top = int(ceil(n ** 0.5))
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, top + 1):
        if n % x == 0:
            return False
    return True


def grid(elementlist, r, c, l=10, style=1):
    if c <= 0 or r <= 0:
        return False
    c, r = c - 1, r
    for x in elementlist:
        if len(str(x)) > l:
            l = len(str(x))
        elif '\n' in str(x):
            return False
    if style == 1:
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = '┃', '━', '┓', '┛', '┏', '┗', '┣', '┫', '┳', '┻', '╋'
    elif style == 2:
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = '║', '═', '╗', '╝', '╔', '╚', '╠', '╣', '╦', '╩', '╬'
    grid = a5 + (a2 * l + a9) * c + a2 * l + a3 + '\n'
    i = 0
    for y in range(r):
        if y > 0:
            grid += a7 + (a2 * l + a11) * c + a2 * l + a8 + '\n'
        for x in range(c + 1):
            try:
                grid += a1 + str(elementlist[i]) + ' ' * (l - len(str(elementlist[i])))
                i += 1
            except:
                grid += a1 + l * ' '
        grid += a1 + '\n'
    grid += a6 + (a2 * l + a10) * c + a2 * l + a4 + '\n'
    return grid


def word_value(strin):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    name = strin.upper()
    z = 0
    for x in name:
        z += 1 + alphabet.index(x)
    return z


def delivers_num(n):
    y = 1
    delivers = []
    while y < n / 2 + 1:
        if n % y == 0:
            delivers.append(y)
        y += 1
    return delivers


def phi(n):
    res = n
    for x in prime_dels_of_num(n):
        res *= (1 - 1 / x)
    return res


'''def phi2(n):
    dels = divisors(n)
    sisi = [1]
    for x in range(2, n):
        if len(list(set(dels) & set(divisors(x)))) == 1:
            sisi.append(x)
    return len(sisi)'''


def relat_prime(a, b):
    if len(list(set(divisors(a)) & set(divisors(b)))) == 1:
        return True
    return False


class Sotfoid:
    count = 0
    library = []

    @staticmethod
    def inner(n):
        '''sum of the factorial of its digits'''
        sn = str(n)
        sum = 0
        for x in sn:
            sum += factorial(int(x))
        return sum

    @staticmethod
    def sotfoid(n):
        if Sotfoid.inner(n) == n or n in Sotfoid.library:
            return 1
        else:
            Sotfoid.library.append(n)
            n = Sotfoid.inner(n)
            Sotfoid.count += 1
            Sotfoid.sotfoid(n)
        return Sotfoid.count

    '''Example
    print(sotfoid(169))
    count=0
    library=[]
    '''


def is_pif(a, b, c):
    lll = [a, b, c]
    q = max(lll)
    lll.remove(q)
    w, r = lll
    if q ** 2 == w ** 2 + r ** 2:
        return True
    return False


def isport(L):
    '''is perimetr of right triangle'''
    '''L=a+b+c
      c^2=a^2+b^2
      c>b>a
      | \
    b|   \ c
      |     \
      |______\
         a
    '''
    count = 0
    d = []
    for b in range(1, ceil(L / 2)):
        for a in range(1, ceil((L - b) / 2)):
            if (L - a - b) ** 2 == a ** 2 + b ** 2:
                d.append([a, b])
                count += 1
                if [b, a] not in d and count > 1:
                    return False
    if count == 0:
        return False
    return True


def prime_dels_of_num(n):
    jopa = []
    for x in delivers_num(n):
        if is_num_prime(x):
            jopa.append(x)
    return jopa


def Fibbonachi(n):
    phi = (1 + 5 ** .5) / 2
    return (phi ** n - (1 - phi) ** n) / (5 ** .5)


# Textableimage
syms = ['█', ' ', '░', '▒', '▓', '╣', '╠']
'''
▒▓=syms[3]+syms[4]
'''


class Field:
    field_sym = syms[1] * 2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = []

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

            print('│')
        for s in range(0, self.width):
            print('――', end='')
        print('╋')


class Point:
    def __init__(self, x, y, f: Field, sym=syms[0] * 2):
        self.x = x
        self.y = y
        self.sym = sym
        self.f = f

    def draw(self):
        self.f.field[self.y][self.x] = self.sym


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
