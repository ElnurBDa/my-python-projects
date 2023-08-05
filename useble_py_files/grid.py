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
