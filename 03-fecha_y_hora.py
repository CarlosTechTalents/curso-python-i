from datetime import datetime

### FECHA Y HORA ACTUALES ###
today = datetime.today()
print(f'{today:%d de %B de %Y}, {today:%H:%m}')

### COMPROBACIÓN DE SEGUNDO PERTENECIENTE A UNA LISTA ###
segundos_magicos = [2, 5, 8, 13, 17, 19, 21, 23, 28, 32, 36, 38, 40, 42, 47, 49, 51, 52, 53, 56, 58]
segundo_actual = datetime.today().second
if segundo_actual in segundos_magicos:
    print(f'\t*** {segundo_actual} ***\n\t¡Este es un segundo mágico!')
else:
    print('\t' + str(segundo_actual) + ' - Sigue jugando, seguro que encuentras tu segundo mágico.')
