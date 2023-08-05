import tkinter as tk

# logs
H = 400
W = 300
bg_color = '#000000'
clr_1='#f222f2'
clr_2='#22f2f2'
# ROOT
root = tk.Tk()
root.title("App")
root.geometry(f"{W}x{H}+300+200")
root.resizable(False, False)
root.config(bg=bg_color)


root.mainloop()
