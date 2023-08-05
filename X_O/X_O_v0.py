

print('Kordinates=>a,b')
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
# 11 12 13 21 22 23 31 32 33
#  5  6  7  9 10 11 13 14 15
#
#  5  6  7
#  9 10 11
# 13 14 15

def r(a, b):
    if a == 1:
        return b + 4
    if a == 2:
        return b + 8
    if a == 3:
        return b + 12

comb = ((5, 6, 7), (9, 10, 11), (13, 14, 15), (5, 9, 13), (6, 10, 14), (7, 11, 15), (5, 10, 15), (7, 10, 13))
count = -1
p = 16
z = [' a\\b', ' 1', ' 2', ' 3',
     ' 1', '', '', '',
     ' 2', '', '', '',
     ' 3', '', '', '', '']
data_x = []
data_o = []
while True:

    count += 1
    if count % 2 == 1:
        z[p] = 'X'
        print(grid(['O'],1,1,4))
    else:
        z[p] = 'O'
        print(grid(['X'],1,1,4))

    pole = grid(z, 4, 4, 4)
    print(pole)

    a = int(input('a= '))
    b = int(input('b= '))
    p = r(a, b)

    if p in data_o or p in data_x:
        print('Error')
        p = 16
        count -= 1

    if count % 2 == 0:
        data_x.append(p)
    else:
        data_o.append(p)

    for x in comb:
        if x[0] in data_x and x[1] in data_x and x[2] in data_x:
            print('━' * 100)
            print('┏'+'━' * 100)
            print('┃ X wins')
            print('┗'+'━' * 100)
            print('━' * 100)
            z = [' a\\b', ' 1', ' 2', ' 3',
                 ' 1', '', '', '',
                 ' 2', '', '', '',
                 ' 3', '', '', '', '']
            data_x = []
            data_o = []
            count-=1
            p=16

        elif x[0] in data_o and x[1] in data_o and x[2] in data_o:
            print('━' * 100)
            print('┏'+'━' * 100)
            print('┃ O wins')
            print('┗'+'━' * 100)
            print('━' * 100)
            z = [' a\\b', ' 1', ' 2', ' 3',
                 ' 1', '', '', '',
                 ' 2', '', '', '',
                 ' 3', '', '', '', '']
            data_x = []
            data_o = []
            count -= 1
            p=16
    print('')
    print('━' * 100)
