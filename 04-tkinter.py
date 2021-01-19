from tkinter import *

root = Tk()
root.title("Carlos")

# Uso de Widgets a través de variables
label_1 = Label(root, text='Car')
label_1.place(x=10, y=10)

label_2 = Label(root, text='los')
label_2.place(x=30, y=30)

# Uso de Widgets directamente
Label(root, text='Car').place(x=10, y=50)
Label(root, text='los').place(x=30, y=70)

root.mainloop()
