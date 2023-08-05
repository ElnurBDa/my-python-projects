from random import randint
from math import floor

iteration = 0
move = "use a s d w"
setka = [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]
setka_up = [[], [], [], [], [0, 1, 2, 3]]
for x in range(0, 16):
    setka_up[x % 4].append(x)
setka_left = [[], [], [], [], [0, 4, 8, 12]]
for x in range(0, 16):
    setka_left[floor(x / 4)].append(x)
setka_right = []
for x in range(0, 4):
    setka_right.append(setka_left[x][::-1])
setka_right.append([3, 7, 11, 15])
setka_down = []
for x in range(0, 4):
    setka_down.append(setka_up[x][::-1])
setka_down.append([0, 1, 2, 3])


def show_it():
    global setka
    x = 0
    while x <= 15:
        if (x + 1) % 4 != 0:
            print(setka[x], end=" | ")
        else:
            print(setka[x])
        x += 1


def up():
    global setka, setka_up
    for x in setka_up[0:4]:
        for i in range(1, 4):
            if setka[x[i]] != 0:
                for u in range(0, i)[::-1]:
                    c = x[u]
                    d = x[u + 1]
                    if setka[c] == 0:
                        setka[c] += setka[d]
                        setka[d] = 0
                    elif setka[c] == setka[d]:
                        setka[c] += setka[d]
                        setka[d] = 0
                        setka[c] = setka[c] + 1 / randint(1000, 2000)


def left():
    global setka, setka_left
    for x in setka_left[0:4]:
        for i in range(1, 4):
            if setka[x[i]] != 0:
                for u in range(0, i)[::-1]:
                    c = x[u]
                    d = x[u + 1]
                    if setka[c] == 0:
                        setka[c] += setka[d]
                        setka[d] = 0
                    elif setka[c] == setka[d]:
                        setka[c] += setka[d]
                        setka[d] = 0
                        setka[c] = setka[c] + 1 / randint(1000, 2000)


def right():
    global setka, setka_right
    for x in setka_right[0:4]:
        for i in range(1, 4):
            if setka[x[i]] != 0:
                for u in range(0, i)[::-1]:
                    c = x[u]
                    d = x[u + 1]
                    if setka[c] == 0:
                        setka[c] += setka[d]
                        setka[d] = 0
                    elif setka[c] == setka[d]:
                        setka[c] += setka[d]
                        setka[d] = 0
                        setka[c] = setka[c] + 1 / randint(1000, 2000)


def down():
    global setka, setka_down
    for x in setka_down[0:4]:
        for i in range(1, 4):
            if setka[x[i]] != 0:
                for u in range(0, i)[::-1]:
                    c = x[u]
                    d = x[u + 1]
                    if setka[c] == 0:
                        setka[c] += setka[d]
                        setka[d] = 0
                    elif setka[c] == setka[d]:
                        setka[c] += setka[d]
                        setka[d] = 0
                        setka[c] = setka[c] + 1 / randint(1000, 2000)


def change_setka(move):
    if move == "w":
        up()
    if move == "a":
        left()
    if move == "d":
        right()
    if move == "s":
        down()


def add_rand_n():
    global setka
    while True:
        i = randint(0, 15)
        if setka[i] == 0:
            setka[i] = 2
            break
        if 0 not in setka:
            break


def clear_setka():
    global setka
    for i in range(0, 16):
        setka[i] = floor(setka[i])


while True:
    print("Iteration" + str(iteration))
    show_it()
    move = input()
    if move != '':
        change_setka(move)
        clear_setka()
        add_rand_n()

        iteration += 1
