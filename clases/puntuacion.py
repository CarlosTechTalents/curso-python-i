from tkinter import *

root = Tk()
root.title("Combates")


class Puntuacion:
    def __init__(self, combatesJugados, combatesGanados, combatesPerdidos, combatesNulos):
        self.combatesJugados = combatesJugados
        self.combatesGanados = combatesGanados
        self.combatesPerdidos = combatesPerdidos
        self.combatesNulos = combatesNulos

    def getPuntuacion(self):

        #   Presentación de datos por consola
        #   print("Jugados: " + str(self.combatesJugados))
        #   print("Ganados: " + str(self.combatesGanados))
        #   print("Perdidos: " + str(self.combatesPerdidos))
        #   print("Nulos: " + str(self.combatesNulos))

        # Presentación de datos por Tkinter

        Label(root, text="*** Combates ***").place(x=30, y=10)
        Label(root, text="Jugados: " + str(self.combatesJugados)).place(x=10, y=30)
        Label(root, text="Ganados: " + str(self.combatesGanados)).place(x=10, y=50)
        Label(root, text="Perdidos: " + str(self.combatesPerdidos)).place(x=10, y=70)
        Label(root, text="Nulos: " + str(self.combatesNulos)).place(x=10, y=90)

    def incrementaCombatesGanados(self):
        self.combatesJugados += 1
        self.combatesGanados += 1

    def incrementaCombatesPerdidos(self):
        self.combatesJugados += 1
        self.combatesPerdidos += 1

    def incrementaCombatesNulos(self):
        self.combatesJugados += 1
        self.combatesNulos += 1
