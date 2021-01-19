from clases.personaje import *

#     def __init__(self, nombre, ataque, vida, estaVivo):

personaje = Personaje("Simón", 100, 2000, True)
enemigo = Personaje("Enemigo", 100, 2000, True)

print("\n*******************************\n")
print(personaje.nombre + " vs. " + enemigo.nombre)

print("\n*******************************\n")
personaje.getCaracteristicas()
print("\n*******************************\n")
enemigo.getCaracteristicas()
print("\n*******************************\n")

daño = enemigo.hacerDaño()
personaje.recibirDaño(daño)

print("Has recibido un ataque de: " + str(daño) + " y ahora te queda de vida: " + str(personaje.vida))
