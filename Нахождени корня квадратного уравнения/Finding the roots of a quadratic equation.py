'''By Elnur'''
from tkinter import *
import datetime

# history
history = open('history.txt', 'r')
history_data = history.read()
history.close()
history = open('history.txt', 'w+')
history.write(history_data + str(datetime.datetime.today()) + '\n \n')
history.close()
count = 0
# colours
bright_theme = '#3863E1'
dark_theme = '#070B16'
warning_color = '#BB0000'
# Menu
root = Tk()
root.resizable(False, False)
root.geometry("400x400+600+200")
xolst = Canvas(root, bg=dark_theme, width=400, height=400, highlightthickness=0)
xolst.pack()
# Exit
exit_btn = Button(xolst, text="Escape", bg=bright_theme, fg=dark_theme)
exit_btn.bind("<Button-1>", lambda event: root.destroy())
exit_btn.place(x=10, y=10)
xolst.bind("<Button-2>", lambda event: root.destroy())
# Entry
a_entry = Entry(xolst, bg=bright_theme, fg=dark_theme)
a_entry.place(x=25, y=50)
b_entry = Entry(xolst, bg=bright_theme, fg=dark_theme)
b_entry.place(x=25, y=75)
c_entry = Entry(xolst, bg=bright_theme, fg=dark_theme)
c_entry.place(x=25, y=100)
# text
xolst.create_text(15, 57, text='a=', font='arial 16', fill=bright_theme)
xolst.create_text(15, 82, text='b=', font='arial 16', fill=bright_theme)
xolst.create_text(15, 107, text='c=', font='arial 16', fill=bright_theme)
xolst.create_text(250, 50, text='ax+bx+c', font='arial 20', fill=bright_theme)
xolst.create_text(230, 40, text='2', font='arial 8', fill=bright_theme)


# Calculate
def calculate(event):
    global count
    data = 'length exceeds 15.'
    xolst.create_rectangle(400, 90, 220, 130, fill=dark_theme, outline=dark_theme)
    xolst.create_rectangle(0, 150, 400, 400, fill=dark_theme, outline=dark_theme)
    if len(a_entry.get()) < 15 and len(b_entry.get()) < 15 and len(c_entry.get()) < 15:
        try:
            data = 'correct value not entered.'
            a = float(a_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            D = b ** 2 - 4 * a * c
            if D < 0:
                data = 'Roots are not real numbers.'
                xolst.create_text(150, 200, text=data, font='arial 16', fill=bright_theme)
            elif D == 0:
                x = -b / (2 * a)
                data = 'X= ' + str(x) + '   .'
                xolst.create_text(150, 200, text=data, font='arial 16', fill=bright_theme)
            else:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                data = 'X1= ' + str(x1) + ',  X2= ' + str(x2) + '   .'
                xolst.create_text(150, 200, text='X1= ' + str(x1) + '\nX2= ' + str(x2) + '   .', font='arial 16',
                                  fill=bright_theme)

        except:
            xolst.create_text(310, 110, text='Enter correct value!', font='arial 14', fill=warning_color)
    else:
        xolst.create_text(210, 210, text='Data length exceeds 15!', font='arial 14', fill=warning_color)
    # history
    count += 1
    history = open('history.txt', 'r')
    history_data = history.read()
    history.close()
    history = open('history.txt', 'w+')
    history.write(history_data + str(count) + ')  ' + data + '\n')
    history.close()
    print(str(count) + ')  ' + data + '\n')


calc_btn = Button(xolst, text="Calculate", bg=bright_theme, fg=dark_theme)
calc_btn.bind("<Button-1>", lambda event: calculate(event))
calc_btn.place(x=160, y=94)

root.mainloop()
