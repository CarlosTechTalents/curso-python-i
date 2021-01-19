import csv

### LECTURA DE UN ARCHIVO CSV ###
with open('08-holamundo.csv', newline='') as archivo:
    datos = csv.reader(archivo, delimiter=',')
    for fila in datos:
        print(fila)

### LECTURA DE UNA ARCHIVO CSV CON CABECERA ###
with open('08-holamundo.csv', newline='') as archivo:
    datos = csv.reader(archivo, delimiter=',')
    contador_lineas = 0
    for fila in datos:
        if contador_lineas == 0:
            print(f'\nNombre de las Columnas:\n\t{", ".join(fila)}\n')
        else:
            print(f'\t{fila[0]} tiene {fila[1]} de ataque y {fila[2]} de vida.')
        contador_lineas += 1
    print(f'Procesadas {contador_lineas} líneas.')

### LECTURA DE UN ARCHIVO CSV POR DICCIONARIO ###
with open('08-holamundo.csv', mode='r', newline='') as archivo:
    datos = csv.DictReader(archivo)
    contador_lineas = 0
    for fila in datos:
        if contador_lineas == 0:
            print(f'\nNombre de las Columnas:\n\t{", ".join(fila)}\n')
        print(f'\t{fila["nombre"]} tiene {fila["ataque"]} de ataque y {fila["vida"]} de vida.')
        contador_lineas += 1
    print(f'Procesadas {contador_lineas} líneas.')

### CREAR UN FICHERO CSV CON CABECERA Y DATOS EN DICCIONARIO ###
with open('08-personajes.csv', mode='w') as archivo:
    cabeceras = ['nombre', 'ataque', 'vida', 'estaVivo']
    datos = csv.DictWriter(archivo, fieldnames=cabeceras)

    datos.writeheader()
    datos.writerow({'nombre': 'Harry Python', 'ataque': '100', 'vida': '2000', 'estaVivo': 'True'})
    datos.writerow({'nombre': 'Rey', 'ataque': '100', 'vida': '2200', 'estaVivo': 'True'})

### ANEXAR DATOS A UN FICHERO CSV ###
with open('08-personajes.csv', mode='a+') as archivo:
    datos = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    datos.writerow(['Reina', '150', '3000', 'True'])
    datos.writerow(['Caballero', '180', '1000', 'True'])
    datos.writerow(['Arquero', '90', '3000', 'True'])
