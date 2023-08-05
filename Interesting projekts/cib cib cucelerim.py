import winsound
from time import sleep as sl
r = 400
do1 = 261
re1 = 293
mi1 = 329
fa1 = 349
sol1 = 392
sol1_=415
la1 = 440
si1 = 493
def do():
    winsound.Beep(do1, r)
def re():
    winsound.Beep(re1, r)
def mi():
    winsound.Beep(mi1, r)
def fa():
    winsound.Beep(fa1, r)
def sol():
    winsound.Beep(sol1, r)
def sol_():
    sol1_
def la():
    winsound.Beep(la1, r)
def si():
    winsound.Beep(si1, r)

def q1():
    do()
    do()
    re()
    mi()
    re()
    do()
def q2():
    do()
    do()
    do()
    do()
    re()
    mi()
    re()
    do()
def q3():
    re()
    re()
    re()
    re()
    mi()
    fa()
    mi()
    re()
def q4():
    re()
    sol()
    fa()
    mi()
    re()
    mi()
    re()
    do()

def w1():
    q1()
    q2()
    q3()
    q4()

def w2():
    mi()
    fa()
    sol()
    sol()
    sol()
    sol_()
    sol()
    fa()
    fa()
    sol()
    sol_()
    sol_()
    sol()
    fa()
    sol()
    mi()
    fa()
    sol()

for x in range(1, 2):
    w1()
    w2()





    sl(1)





