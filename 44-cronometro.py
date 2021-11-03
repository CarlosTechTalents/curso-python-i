from tkinter import *

ventana = Tk()
ventana.title("Cronometro")

t = 0
s = 0
n = 0
while 1 != 2:
    import time
    tiempo_segundos = time.time()
    ''''print(tiempo_segundos)''' ''
    tiempo_cadena = time.ctime(tiempo_segundos)  # 1488651001.7188754 seg
    x = (tiempo_cadena[17] + tiempo_cadena[18])
    x = int(x)
    ''''print(x)''' ''
    a = 0
    if x > s:
        a = 1
    t = t + a
    if t > n:
        print(t)
        texto1 = Label(ventana, text=t)
        texto1.grid(row=1, column=1)

    s = x
    n = t

ventana.mainloop()