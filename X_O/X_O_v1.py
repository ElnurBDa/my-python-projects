from tkinter import *

position = 9
data_x = []
data_o = []
count = 0
'''
012
345
678'''
comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
win = Tk()
win.resizable(False, False)
win.geometry('400x300+600+200')

X_point = 0
O_point = 0
while True:
    xolst = Canvas(win, bg='#B8B8B8', width=400, height=300, highlightthickness=0)
    xolst.pack()
    for x in range(0, 4):
        xolst.create_line(0, x * 100, 300, x * 100, width=3)
        xolst.create_line(x * 100, 0, x * 100, 300, width=3)
    aa = 'XO'
    xolst.create_rectangle(350, 0, 390, 20, fill='#B8B8B8')
    xolst.create_text(370, 10, text=aa[count % 2])
    xolst.create_rectangle(350, 50, 390, 90, fill='#B8B8B8')
    xolst.create_text(370, 65, text=str(X_point) + '-' + str(O_point))
    xolst.create_text(370, 80, text='X-O')


    def pr(event):
        x = event.x
        y = event.y
        global position, a, b, data_x, data_o, count, win, X_point, O_point
        qqqq = 'XO'
        gggg = 'OX'
        text = qqqq[count % 2]
        text_ = gggg[count % 2]
        if x <= 100:
            if y <= 100:
                position = (0)
            if y <= 200 and y > 100:
                position = (3)
            if y <= 300 and y > 200:
                position = (6)
        if x <= 200 and x > 100:
            if y <= 100:
                position = (1)
            if y <= 200 and y > 100:
                position = (4)
            if y <= 300 and y > 200:
                position = (7)
        if x <= 300 and x > 200:
            if y <= 100:
                position = (2)
            if y <= 200 and y > 100:
                position = (5)
            if y <= 300 and y > 200:
                position = (8)
        if x >= 300:
            position = 9
        a, b = -100, -100
        if position == 0:
            a, b = 50, 50
        if position == 1:
            a, b = 150, 50
        if position == 2:
            a, b = 250, 50
        if position == 3:
            a, b = 50, 150
        if position == 4:
            a, b = 150, 150
        if position == 5:
            a, b = 250, 150
        if position == 6:
            a, b = 50, 250
        if position == 7:
            a, b = 150, 250
        if position == 8:
            a, b = 250, 250

        if position in data_o or position in data_x:
            position = 9
        else:
            count += 1
            if text == 'X':
                data_x.append(position)
            else:
                data_o.append(position)
            xolst.create_rectangle(a - 20, b - 20, a + 20, b + 20, fill='#B8B8B8')
            xolst.create_text(a, b, text=text)

            xolst.create_rectangle(350, 0, 390, 20, fill='#B8B8B8')
            xolst.create_text(370, 10, text=text_)

        if len(data_x) + len(data_o) == 9:
            for l in range(0, 3):
                for r in range(0, 3):
                    xolst.create_rectangle(l * 100 + 30, r * 100 + 30, l * 100 + 70, r * 100 + 70, fill='#B8B8B8')
            data_x = []
            data_o = []

        print(position, a, b, data_x, data_o)
        for x in comb:
            if x[0] in data_x and x[1] in data_x and x[2] in data_x:
                data_x = []
                data_o = []
                position = 9
                X_point += 1
                for l in range(0, 3):
                    for r in range(0, 3):
                        xolst.create_rectangle(l * 100 + 30, r * 100 + 30, l * 100 + 70, r * 100 + 70, fill='#B8B8B8')
                xolst.create_rectangle(350, 50, 390, 90, fill='#B8B8B8')
                xolst.create_text(370, 65, text=str(X_point) + '-' + str(O_point))
                xolst.create_text(370, 80, text='X-O')
            elif x[0] in data_o and x[1] in data_o and x[2] in data_o:
                data_x = []
                data_o = []
                position = 9
                O_point += 1
                for l in range(0, 3):
                    for r in range(0, 3):
                        xolst.create_rectangle(l * 100 + 30, r * 100 + 30, l * 100 + 70, r * 100 + 70, fill='#B8B8B8')
                xolst.create_rectangle(350, 50, 390, 90, fill='#B8B8B8')
                xolst.create_text(370, 65, text=str(X_point) + '-' + str(O_point))
                xolst.create_text(370, 80, text='X-O')


    xolst.bind('<Button-1>', pr)

    win.mainloop()
