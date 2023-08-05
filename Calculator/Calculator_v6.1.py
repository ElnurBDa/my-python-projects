from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# calculato_v6
w1 = Tk()
w1.geometry("240x200+1350+10")
w1.resizable(False,False)
w1.title("Calculator")


def calc(key):
    global memory
    if key == '=':
        str1 = '1234567890-+*/.'
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "One of symbols isn't a digit . ")
            messagebox.showerror("Error!", "Enter right symbol!")
            calc_entry.delete(0, END)
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Data isn't right!")
            calc_entry.delete(0, END)
    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == '+/-':
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    elif key == 'Click me!':
        calc_entry.delete(0, END)
        calc_entry.insert(END, "Elnur is great")
    elif key == 'don\'t try!':
        calc_entry.delete(0, END)
        calc_entry.insert(END, "You are a STUPID!")
    elif key == 'Info.':
        calc_entry.delete(0, END)
        calc_entry.insert(END, "Created by Elnur.Calculator_v6.1|09|09|2019")
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


button_list = [
    'C', '=', '.',
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '+', '0', '-',
    '*', '+/-', '/',
    'Click me!', 'don\'t try!', 'Info.'
]

r = 1
c = 0
for i in button_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(w1, text=i, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

calc_entry = Entry(w1, width=38)
calc_entry.grid(row=0, column=0, columnspan=5)
w1.mainloop()
