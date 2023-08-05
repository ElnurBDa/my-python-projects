from tkinter import *
import math
# okoshko
w1 = Tk()
w1.title("Калькулятор")
w1.geometry("400x400")
# xolst
xolst = Canvas(w1, width=400, height=400, bg="#999")
xolst.pack(side="left")
# info xolst
info_xolst = Canvas(w1, width=40000, height=6000, bg="green")
info_xolst.pack(side="right")
info_xolst.create_text(100, 300, text="Calculator_v4\nСоздан Бадаловым Эльнуром\n31.08.2019", fill="yellow")
# xolst ...
xolst.create_text(200, 10, text="Калькулятор", )
xolst.create_text(200, 25, text=" + , - , / , * ,^ ", )
label_1 = Label(w1, text="Введите первое число : ", bg="#999")
label_1.place(x=30, y=150)
label_2 = Label(w1, text="Введите второе число : ", bg="#999")
label_2.place(x=30, y=180)
label_op = Label(w1, text="Введите операцию       : ", bg="#999")
label_op.place(x=30, y=210)

entry_1 = Entry(w1, bg="#998")
entry_1.place(x=160, y=152)
entry_2 = Entry(w1, bg="#998")
entry_2.place(x=160, y=182)
entry_op = Entry(w1, bg="#998")
entry_op.place(x=160, y=212)

def calc(a , b , op):
    if op == "+" :
        r= float(a) + float(b)
        label_otvet = Label(w1, text="Ответ:    " + str(r), bg="#997" , width = 20 , height = 5)
        label_otvet.place(x=150, y=50)
    if op == "-" :
        r= float(a) - float(b)
        label_otvet = Label(w1, text="Ответ:    " + str(r), bg="#998", width = 20 , height = 5)
        label_otvet.place(x=150, y=50)
    if op == "*" :
        r= float(a) * float(b)
        label_otvet = Label(w1, text="Ответ:    " + str(r), bg="#998", width = 20 , height = 5)
        label_otvet.place(x=150, y=50)
    if op == "/" :
        r= float(a) / float(b)
        label_otvet = Label(w1, text="Ответ:    " + str(r), bg="#998", width = 20 , height = 5)
        label_otvet.place(x=150, y=50)
    if op == "^" :
        r= float(a)**float(b)
        label_otvet = Label(w1, text="Ответ:    " + str(r), bg="#998", width = 20 , height = 5)
        label_otvet.place(x=150, y=50)




button_calculator = Button(w1, text="Рассчитать", width=17, bg="#998")
button_calculator.bind("<Button-1>", lambda event : calc(entry_1.get() , entry_2.get() , entry_op.get()))
button_calculator.place(x=158, y=250)

w1.mainloop()
