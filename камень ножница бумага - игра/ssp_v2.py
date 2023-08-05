# ssp_v2

import random
from tkinter import *

# okoshko
w1 = Tk()
w1.title("Stone/Scissors/Paper")
w1.geometry("800x600")
# xolst
xolst = Canvas(w1, width=800, height=600, bg="#66CDAA")
xolst.pack(side="left")
# xolst info
xolst_info = Canvas(w1, width=300, height=5000, bg="#FAEBD7")
xolst_info.pack(side="right")
xolst_info.create_text(100, 100, text="SSP_v2\nCreated by Elnur Badalov\n04.09.2019", fill="black")
# xolst
xolst.create_text(400, 20, text="Stone/Scissors/Paper", font='arial 20')
xolst.create_text(400, 400, text="Chose one of them.", font='arial 20')


def elnur(x):
    app = random.randint(1, 3)
    if app == 1:
        e = "Stone"
    elif app == 2:
        e = "Scissors"
    else:
        e = "Paper"
    if x == 1:
        ti_vbral = Label(xolst, text="You chose Scissors\nKomputer choses " + e, width=20, height=3, bg='#008B8B',
                         fg='white', font='arial 20')
        ti_vbral.place(x=250, y=100)
        if app == 1:
            result = Label(xolst, text="Komputer win \n You lose!", width=20, height=3, bg='#8B0000',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
        elif app == 2:
            result = Label(xolst, text="Draw", width=20, height=3, bg='#006400',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
        elif app == 3:
            result = Label(xolst, text="You win !", width=20, height=3, bg='#00FFFF',
                           fg='black', font='arial 20')
            result.place(x=250, y=200)
    if x == 2:
        ti_vbral = Label(xolst, text="You chose Stone\nKomputer choses " + e, width=20, height=3, bg='#008B8B',
                         fg='white', font='arial 20')
        ti_vbral.place(x=250, y=100)
        if app == 1:
            result = Label(xolst, text="Draw", width=20, height=3, bg='#006400',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
        elif app == 2:
            result = Label(xolst, text="You win !", width=20, height=3, bg='#00FFFF',
                           fg='black', font='arial 20')
            result.place(x=250, y=200)
        elif app == 3:
            result = Label(xolst, text="Komputer win \n You lose!", width=20, height=3, bg='#8B0000',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
    if x == 3:
        ti_vbral = Label(xolst, text="You chose Paper\nKomputer choses " + e, width=20, height=3, bg='#008B8B',
                         fg='white', font='arial 20')
        ti_vbral.place(x=250, y=100)
        if app == 1:
            result = Label(xolst, text="You win !", width=20, height=3, bg='#00FFFF',
                           fg='black', font='arial 20')
            result.place(x=250, y=200)
        elif app == 2:
            result = Label(xolst, text="Komputer win \n You lose!", width=20, height=3, bg='#8B0000',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
        elif app == 3:
            result = Label(xolst, text="Draw", width=20, height=3, bg='#006400',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)


scissors = Button(xolst, text='scissors', width=10, height=3, bg='#008B8B', fg='white', font='arial 20')
scissors.bind("<Button-1>", lambda event: elnur(1))
scissors.place(x=50, y=450)
stone = Button(xolst, text='stone', width=10, height=3, bg='#008B8B', fg='white', font='arial 20')
stone.bind("<Button-1>", lambda event: elnur(2))
stone.place(x=300, y=450)
paper = Button(xolst, text='paper', width=10, height=3, bg='#008B8B', fg='white', font='arial 20')
paper.bind("<Button-1>", lambda event: elnur(3))
paper.place(x=550, y=450)

w1.mainloop()
