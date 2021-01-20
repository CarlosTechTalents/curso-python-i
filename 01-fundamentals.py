#########################################
# Preparación del entorno de desarrollo #
#########################################

# Descargar el interprete de Python de https://www.python.org/downloads/
# Instalar marcando el check Add Python to PATH

# Descargar Visual Studio Code de https://code.visualstudio.com/download
# Instalar Visual Studio Code
# Instalar la extension Python extension for Visual Studio Code del desarrollador Microsoft

# Crear la carpeta del proyecto
# Abrir la carpeta del proyecto
# Crear un archivo main.py
# Crear un hola mundo con print("Hola mundo")
# Ejecutamos con el botón derecho sobre el código con la opción Run Python File in Terminal

#############
# Variables #
#############

# Son espacios reservados.
# Se componen de un nombre y un valor.
# El valor varia a lo largo de la ejecución del programa.
# El nombre de la variable se escribe en minúsculas.
# Tipos de variables: String: texto entre comillas, Integer: número entero, Boolean: True o False, Float: número decimal con un punto.

nombre = "Carlos"
ataque = 11
vida = 200
estaVivo = True

#########
# Input #
#########

nombre = input("¿Cómo te llamas?: ")

#################
# Condicionales #
#################

if nombre == "Carlos":
    if vida >= 100:
        print("Hola, soy " + nombre + " y tengo " + str(vida) + " vida.")
    else:
        print("¿Estás vivo?")
else:
    print("Entonces, ¿Quien eres?")
print("Hasta luego.")

###############
# Bucle while #
###############

contadorWhile = 0
while contadorWhile < 10:
    print(contadorWhile)
    contadorWhile = contadorWhile + 1
print("Fin del bucle While")

#############
# Bucle for #
#############

for contadorFor in range(0, 5):
    print(contadorFor)
print("Fin del bucle For")

##########################
# Función sin parámetros #
##########################


def saludo():
    print("¡Saludos a secas!")


saludo()

##########################
# Función con parámetros #
##########################


def saludoNombre(nombreParametro):
    print("¡Saludos " + nombreParametro + " !")


saludoNombre("tu nombre")
saludoNombre(nombre)

######################################
# Función con retorno sin parámetros #
######################################


def inputEdad():
    return input("¿Cuantos años tienes?: ")


edad = int(inputEdad())
print("Tienes : " + str(edad) + " años")

######################################
# Función con retorno con parámetros #
######################################


def anoNacimiento(edadParametro):
    return 2020 - edadParametro


print("Naciste en " + str(anoNacimiento(edad)))

##########
# Listas #
##########

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
print(meses)

meses.append("Septiembre")
meses.append("Octubre")
print(meses)

meses.insert(6, "Julio")
meses.insert(7, "Agosto")
print(meses)

meses.remove("Febrero")
print(meses)

meses.pop(2)
print(meses)

print(meses[5])

for i in meses:
    print(i)

#########
# Tupla #
#########

coloresRGB = ("Rojo", "Verde", "Azul")
coloresCMYK = ("Cian", "Magenta", "Amarillo", "Negro")
colores = coloresRGB + coloresCMYK
print("Colores RGB: " + str(coloresRGB))
print("Colores CMYK: " + str(coloresCMYK))
print("Todos los colores: " + str(colores))

print("El color RGB que se parece al Cian es: " + coloresRGB[2])

for i in colores:
    print(i)

###############
# Diccionario #
###############

coordenadas = {"x": 2, "y": 3, "z": 4}
print(coordenadas)
coordenadas["time"] = "3600sg"
print(coordenadas)

print("x: " + str(coordenadas["x"]))
print("tiempo: " + coordenadas["time"])

del coordenadas["z"]
print("Coordenadas en 2D: " + str(coordenadas))

for i in coordenadas:
    print(str(i) + ":" + str(coordenadas[i]))
