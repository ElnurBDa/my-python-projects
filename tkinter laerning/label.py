import tkinter as tk

# logs
H = 400
W = 300
bg_color = '#12af3b'
clr_1 = '#f222f2'
clr_2 = '#22f2f2'
# ROOT
root = tk.Tk()
root.title("App")
root.geometry(f"{W}x{H}+300+200")
root.resizable(False, False)
root.config(bg=bg_color)

l1 = tk.Label(root, text="U\nR\nGREAT!",
              bg=clr_2,
              fg=clr_1,
              font=('', 20, 'bold'),
              padx=20,
              pady=20,  # в пикселях
              width=12,  # в знаках
              height=7,
              anchor='nw',
              relief=tk.RAISED,
              bd=30,
              justify=tk.LEFT
              )
l1.pack()

root.mainloop()
