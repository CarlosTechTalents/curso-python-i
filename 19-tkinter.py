from tkinter import *

root = Tk()
root.title("Carlos")
root.geometry("500x500")

Label(root, text='Car').place(x=10, y=10)
Label(root, text='los').place(x=20, y=40)

frame1 = Frame(root, width=50, height=30, bg="green")
frame1.pack(side=LEFT)

frame2 = Frame(root, width=50, height=30, bg="blue")
frame2.pack(side=RIGHT)

rectangle_1 = Label(root, text="Rojo", bg="red", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

button_1 = Button(root, text="Botón Zito")
button_1.pack(side=LEFT)

rectangle_2 = Label(root, text="Amarillo", bg="yellow", fg="black")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

Label(root, text="Hello World!").pack()

Label(root, text='Car').place(x=100, y=10)
Label(root, text='los').place(x=110, y=40)

root.mainloop()
