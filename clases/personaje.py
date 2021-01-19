import random


class Personaje:
    def __init__(self, nombre, ataque, vida, estaVivo):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.estaVivo = estaVivo

    def getCaracteristicas(self):
        print("----------\nNombre del personaje: " + self.nombre + "\nAtaque: " + str(self.ataque) + "\nVida: " + str(self.vida) + "\nEstá vivo: " + str(self.estaVivo) + "\n----------\n")

    def hacerDaño(self):
        aleatoria = random.randint(0, 100)
        daño = self.ataque + aleatoria
        return daño

    def recibirDaño(self, daño):
        self.vida = self.vida - daño
