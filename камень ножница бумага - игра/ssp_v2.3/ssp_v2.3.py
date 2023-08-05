# ssp_v2.3
import random
from tkinter import *
import time

# okoshko
w1 = Tk()
w1.title("Stone/Scissors/Paper")
w1.geometry("800x600")
w1.minsize(800, 600)
w1.maxsize(1000, 600)
# xolst
xolst = Canvas(w1, width=800, height=600, bg="#66CDAA")
xolst.pack(side="left")
# xolst info
xolst_info = Canvas(w1, width=300, height=5000, bg="#66CDAA")
xolst_info.pack(side="right")
xolst_info.create_text(100, 100, text="SSP_v2.3\nCreated by Elnur Badalov\n04.09.2019", fill="black")
# xolst
xolst.create_text(400, 20, text="Stone/Scissors/Paper", font='arial 20')
xolst.create_text(400, 400, text="Chose one of them.", font='arial 20')
# images
image_scissors = PhotoImage(
    file='C:\\Users\\User\\PycharmProjects\\камень ножница бумага - игра\\ssp_v2.3\\scissors.gif')
image_stone = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\камень ножница бумага - игра\\ssp_v2.3\\stone.gif')
image_paper = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\камень ножница бумага - игра\\ssp_v2.3\\paper.gif')


def elnur(x):
    time.sleep(0.2)
    app = random.randint(1, 3)
    label_vraq_choise = Label(text="Computer choose:", font='arial 15', bg='#66CDAA')
    label_vraq_choise.place(x=600, y=60)
    if app == 1:
        e = "Stone"
        a = Label(width=25, height=20, bg='#66CDAA')
        a.place(x=650, y=2)
        kartina = Label(image=image_stone, bg='#008B8B')
        kartina.place(x=650, y=100)
    elif app == 2:
        e = "Scissors"
        a = Label(width=25, height=20, bg='#66CDAA')
        a.place(x=650, y=2)
        kartina = Label(image=image_scissors, bg='#008B8B')
        kartina.place(x=650, y=100)
    else:
        e = "Paper"
        a = Label(width=25, height=20, bg='#66CDAA')
        a.place(x=650, y=2)
        kartina = Label(image=image_paper, bg='#008B8B')
        kartina.place(x=650, y=100)
    if x == 1:
        ti_vbral = Label(xolst, text="You chose Scissors\nСomputer choses " + e, width=20, height=3, bg='#008B8B',
                         fg='white', font='arial 20')
        ti_vbral.place(x=250, y=100)
        if app == 1:
            result = Label(xolst, text="Сomputer win \n You lose!", width=20, height=3, bg='#8B0000',
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
        ti_vbral = Label(xolst, text="You chose Stone\nСomputer choses " + e, width=20, height=3, bg='#008B8B',
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
            result = Label(xolst, text="Сomputer win \n You lose!", width=20, height=3, bg='#8B0000',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
    if x == 3:
        ti_vbral = Label(xolst, text="You chose Paper\nСomputer choses " + e, width=20, height=3, bg='#008B8B',
                         fg='white', font='arial 20')
        ti_vbral.place(x=250, y=100)
        if app == 1:
            result = Label(xolst, text="You win !", width=20, height=3, bg='#00FFFF',
                           fg='black', font='arial 20')
            result.place(x=250, y=200)
        elif app == 2:
            result = Label(xolst, text="Сomputer win \n You lose!", width=20, height=3, bg='#8B0000',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)
        elif app == 3:
            result = Label(xolst, text="Draw", width=20, height=3, bg='#006400',
                           fg='white', font='arial 20')
            result.place(x=250, y=200)


# Buttons
scissors = Button(xolst, text='scissors', bg='#008B8B', fg='white', font='arial 20', image=image_scissors)
scissors.bind("<Button-1>", lambda event: elnur(1))
scissors.place(x=50, y=450)
stone = Button(xolst, text='stone', bg='#008B8B', fg='white', font='arial 20', image=image_stone)
stone.bind("<Button-1>", lambda event: elnur(2))
stone.place(x=300, y=450)
paper = Button(xolst, text='paper', bg='#008B8B', fg='white', font='arial 20', image=image_paper)
paper.bind("<Button-1>", lambda event: elnur(3))
paper.place(x=550, y=450)
w1.mainloop()
