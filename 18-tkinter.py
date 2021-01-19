import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Carlos")
root.geometry("600x400")

label_1 = ttk.Label(root, text="Hello Label!", padding=(30, 10))
label_1.place(x=50, y=50)
label_1.pack()

rectangle_1 = tk.Label(root, text="Rojo", bg="red", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()

rectangle_2 = tk.Label(root, text="Amarillo", bg="yellow", fg="black")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Verde", bg="green", fg="black")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()
ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()
ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()

print("Hello World!")

root.mainloop()
