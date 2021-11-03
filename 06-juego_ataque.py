from clases.personaje import *
from clases.puntuacion import *
import random
import sys

##### INSTANCIAS DE PERSONAJES DEL EQUIPO Y DE PUNTUACIÓN #####

# La clase Personaje está definida así: def __init__(self, nombre, ataque, vida, estaVivo):

rey = Personaje("Rey", 120, 2000, True)
reina = Personaje("Reina", 90, 3000, True)
caballero = Personaje("Caballero", 140, 1500, True)
arquero = Personaje("Arquero", 40, 5000, True)

equipo = {"rey": rey, "reina": reina, "caballero": caballero, "arquero": arquero}

# La clase Puntuacion está definida así: def __init__(self, combatesJugados, combatesGanados, combatesPerdidos, combatesNulos):

puntuacion = Puntuacion(0, 0, 0, 0)
puntuacion.getPuntuacion()

##### FUNCIÓN LUCHAR #####


def luchar(luchador, oponente):

    lucha = True

    # Establece si el primer turno es del jugador o del oponente
    turno = random.randint(0, 1)

    while (lucha):
        if (turno == 0):
            daño = luchador.hacerDaño()
            oponente.recibirDaño(daño)
            turno = 1
        else:
            daño = oponente.hacerDaño()
            luchador.recibirDaño(daño)
            turno = 0

        if (luchador.vida <= 0 or oponente.vida <= 0):
            lucha = False

    if (luchador.vida > 0):
        print("\n**********\n¡Enhorabuena, has ganado!\nTienes " + str(luchador.vida) + " vida\nY tu enemigo tiene " + str(oponente.vida) + " vida\n**********\n")
        puntuacion.incrementaCombatesGanados()
    else:
        print("\n**********\n¡Lo siento, has perdido!\nTienes " + str(luchador.vida) + " vida\nY tu enemigo tiene " + str(oponente.vida) + " vida\n**********\n")
        luchador.estaVivo = False
        puntuacion.incrementaCombatesPerdidos()

    puntuacion.getPuntuacion()


##### COMIENZO DEL JUEGO #####

inicio = True

while (inicio):
    opcion = input("\nIntroduce una opción:\n  1.Luchar\n  2.Ver Puntuación\n  3.Salir\n  4.Salir con sys.exit\n\nTu opción: ")

    if opcion == "1":

        print("\n*** Combate Nº: " + str(puntuacion.combatesJugados + 1) + " ***\n")
        puntuacion.getPuntuacion()

        print("\n\n*** TU ENEMIGO ***")
        enemigo = Personaje("Orco", random.randint(100, 150), random.randint(1500, 2500), True)
        enemigo.getCaracteristicas()

        print("\n*** TU EQUIPO ***")
        for i in equipo:
            print(str(i) + ": ")
            equipo[i].getCaracteristicas()

        print("¿Con quién vas a luchar?:")

        for i in equipo:
            if (equipo[i].estaVivo):
                print("-" + str(i))

        clave = input("\nTu opción: ")

        if clave in equipo and equipo[clave].estaVivo:
            luchar(equipo[clave], enemigo)
        else:
            print("Opción no valida")
            puntuacion.incrementaCombatesNulos()
            puntuacion.getPuntuacion()

    elif opcion == "2":
        print("\n***** PUNTUACIÓN DESPUÉS DE " + str(puntuacion.combatesJugados) + " COMBATES *****")
        puntuacion.getPuntuacion()

    elif opcion == "3":
        print("\n***** FIN DE LA PARTIDA *****")
        puntuacion.getPuntuacion()
        inicio = False

    elif opcion == "4":
        print("\n***** FIN DE LA PARTIDA *****")
        puntuacion.getPuntuacion()
        sys.exit()
