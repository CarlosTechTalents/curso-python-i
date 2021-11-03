from datetime import datetime

### FECHA Y HORA ACTUALES ###
today = datetime.today()
print(f'{today:%d de %B de %Y}, {today:%H:%m}')

### COMPROBACIÓN DE SEGUNDO PERTENECIENTE A UNA LISTA ###

# Dos formas de pasar el txt a una lista, primera: #
segundos_magicos = []
archivo = open('10-segundos_magicos.txt', 'r')
leer_lineas = archivo.readlines()
archivo.close()
for linea in leer_lineas:
    segundos_magicos.append(linea.strip())
print(segundos_magicos)

# Dos formas de pasar el txt a una lista, segunda: #
with open('10-segundos_magicos.txt', 'r') as archivo:
    segundos_magicos = [linea.strip() for linea in archivo]
print(segundos_magicos)

segundo_actual = str(datetime.today().second)
if segundo_actual in segundos_magicos:
    print(f'\t*** {segundo_actual} ***\n\t¡Este es un segundo mágico!')
else:
    print(f'\tEl {segundo_actual} no está en la lista\n\t>>> Sigue jugando, seguro que encuentras tu segundo mágico <<<')
