from tkinter import *
import math

# okoshko
w1 = Tk()
w1.title("Калькулятор")
w1.geometry("400x300")
# xolst
xolst = Canvas(w1, width=400, height=300, bg="#999")
xolst.pack(side="left")
# info xolst
info_xolst = Canvas(w1, width=40000, height=6000, bg="green")
info_xolst.pack(side="right")
info_xolst.create_text(100, 100, text="Calculator_v5.1\nСоздан Бадаловым Эльнуром\n31.08.2019", fill="yellow")
# xolst ...
xolst.create_text(200, 10, text="Калькулятор")
# надписи-указатели
label_za_otvetom = Label(xolst, bg="#997", width=50, height=3)
label_za_otvetom.place(x=20, y=50)
label_1 = Label(xolst, text="Введите первое число : ", bg="#999")
label_1.place(x=30, y=150)
label_2 = Label(xolst, text="Введите второе число : ", bg="#999")
label_2.place(x=30, y=180)
# места ввода
entry_1 = Entry(xolst, bg="#998")
entry_1.place(x=160, y=152)
entry_2 = Entry(xolst, bg="#998")
entry_2.place(x=160, y=182)
# кнопки над простыми операциями
btn = Button(xolst, text="+", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_plus(entry_1.get(), entry_2.get()))
btn.place(x=30, y=205)
btn = Button(xolst, text="-", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_minus(entry_1.get(), entry_2.get()))
btn.place(x=100, y=205)
btn = Button(xolst, text="/", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_deleniye(entry_1.get(), entry_2.get()))
btn.place(x=170, y=205)
btn = Button(xolst, text="*", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_umnojeniye(entry_1.get(), entry_2.get()))
btn.place(x=240, y=205)
btn = Button(xolst, text="^", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_vozvedenie_v_stepen(entry_1.get(), entry_2.get()))
btn.place(x=310, y=205)
# кнопки тригонометричесских операций
btn = Button(xolst, text="sin", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_sin(entry_1.get(), entry_2.get()))
btn.place(x=30, y=235)
btn = Button(xolst, text="cos", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_cos(entry_1.get(), entry_2.get()))
btn.place(x=100, y=235)
btn = Button(xolst, text="tan", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_tan(entry_1.get(), entry_2.get()))
btn.place(x=170, y=235)
btn = Button(xolst, text="cot", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_cot(entry_1.get(), entry_2.get()))
btn.place(x=240, y=235)
btn = Button(xolst, text="!", width=7, bg="#998")
btn.bind("<Button-1>", lambda event: funk_factorial(entry_1.get(), entry_2.get()))
btn.place(x=310, y=235)


# операции над числами
def funk_plus(a, b):
    result = float(a) + float(b)
    label_otvet = Label(xolst, text="Ответ:    " + str(result), bg="#997", width=30, height=3)
    label_otvet.place(x=100, y=50)


def funk_minus(a, b):
    result = float(a) - float(b)
    label_otvet = Label(xolst, text="Ответ:    " + str(result), bg="#997", width=30, height=3)
    label_otvet.place(x=100, y=50)


def funk_deleniye(a, b):
    result = float(a) / float(b)
    label_otvet = Label(xolst, text="Ответ:    " + str(result), bg="#997", width=30, height=3)
    label_otvet.place(x=100, y=50)


def funk_umnojeniye(a, b):
    result = float(a) * float(b)
    label_otvet = Label(xolst, text="Ответ:    " + str(result), bg="#997", width=30, height=3)
    label_otvet.place(x=100, y=50)


def funk_vozvedenie_v_stepen(a, b):
    result = float(a) ** float(b)
    label_otvet = Label(xolst, text="Ответ:    " + str(result), bg="#997", width=30, height=3)
    label_otvet.place(x=100, y=50)


# Тригонометрия
def funk_sin(a, b):
    result = math.sin(float(a))
    label_otvet_1 = Label(xolst, text="Ответ первого:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_1.place(x=100, y=50)
    result = math.sin(float(b))
    label_otvet_2 = Label(xolst, text="Ответ второго:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_2.place(x=100, y=70)


def funk_cos(a, b):
    result = math.cos(float(a))
    label_otvet_1 = Label(xolst, text="Ответ первого:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_1.place(x=100, y=50)
    result = math.cos(float(b))
    label_otvet_2 = Label(xolst, text="Ответ второго:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_2.place(x=100, y=70)


def funk_tan(a, b):
    result = math.tan(float(a))
    label_otvet_1 = Label(xolst, text="Ответ первого:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_1.place(x=100, y=50)
    result = math.tan(float(b))
    label_otvet_2 = Label(xolst, text="Ответ второго:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_2.place(x=100, y=70)


def funk_cot(a, b):
    result = math.cos(float(a)) / math.sin(float(a))
    label_otvet_1 = Label(xolst, text="Ответ первого:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_1.place(x=100, y=50)
    result = math.cos(float(b)) / math.sin(float(b))
    label_otvet_2 = Label(xolst, text="Ответ второго:    " + str(result), bg="#997", width=30, height=1)
    label_otvet_2.place(x=100, y=70)


# факториал
def funk_factorial(a, b):
    result = math.factorial(float(a))
    label_otvet_1 = Label(xolst, text="Ответ первого:    " + str(result), bg="#997", width=50, height=1)
    label_otvet_1.place(x=20, y=50)
    result = math.factorial(float(b))
    label_otvet_2 = Label(xolst, text="Ответ второго:    " + str(result), bg="#997", width=50, height=1)
    label_otvet_2.place(x=20, y=70)


w1.mainloop()
