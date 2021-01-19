from datetime import datetime
hora_actual = datetime.today()

### LEER UN ARCHIVO DE TEXTO ###
archivo = open('07-holamundo.txt', 'r')
texto = archivo.read()
archivo.close()

print("*** 1.- Lectura del archivo original ***")
print(texto)
print('\n')

### ANEXAR A UN ARCHIVO DE TEXTO ###
archivo = open('07-holamundo.txt', 'a')
archivo.write('\n' + 'Hola Mundo anexado V2.0')
archivo.close()

archivo = open('07-holamundo.txt', 'r')
texto = archivo.readlines()
archivo.close()

print("*** 2.- Lectura del archivo después de añadir una línea ***")
for i in range(0, len(texto)):
    print(str(i) + '.-' + texto[i])
print('\n')

### MODIFICAR UNA LINEA DE UN ARCHIVO DE TEXTO ###
archivo = open('07-holamundo.txt', 'r+')
texto = archivo.readlines()
print('El archivo tiene ' + str(len(texto)) + ' líneas')
print('Si existe voy a modificar la línea 3')

# Modificamos la línea que queramos a partir del índice
if len(texto) > 3:
    texto[2] = 'Esta es la línea 3 modificada a las ' + str(hora_actual) + '\n'

# Volvemos a ponter el puntero al inicio y reescribimos
archivo.seek(0)
archivo.writelines(texto)
archivo.close()

# Leemos el fichero de nuevo usando el statement with. Con with no hace falta cerrar el archivo, ya lo hace él cuando acaba de usarlo.
print("*** 3.- Lectura del archivo después de modificar la línea 3 ***")
with open("07-holamundo.txt", "r") as archivo:
    print(archivo.read())
print('\n')

### CREACIÓN Y MODIFICACIÓN DE UN ARCHIVO DE TEXTO ###
# Creamos un fichero de prueba con 4 líneas
print("*** 4.- Creación y modificación de un archivo nuevo ***")
fichero = open('07-holamundo2.txt', 'w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('07-holamundo2.txt', 'r+')
fichero.write("0123456")

# Volvemos a ponter el puntero al inicio y leemos hasta el final
fichero.seek(0)
print(fichero.read())
fichero.close()