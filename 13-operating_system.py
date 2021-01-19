import os

print('\n*** IDENTIFICACIÓN DEL SISTEMA OPERARTIVO ***')
print(os.uname())

print('\n*** MUESTRA LAS VARIABLES DE ENTORNO ***')
for k, v in os.environ.items():
    print(f'{k}={v}')

print('\n*** MOSTRAR VALORES CONCRETROS DE VARIABLES DE ENTORNO: USER Y HOME ***')
home_dir = os.environ['HOME']
username = os.environ['USER']

print(f'{username} el directorio de trabajo es {home_dir}')

print('\n*** CREA VARIABLES DE ENTORNO ***')
env_var = input('Introduce el nombre de la variable de entorno que quieres crear:\n')
env_var_value = input('Introduce el valor de la variable de entorno que has creado:\n')
os.environ[env_var] = env_var_value
print(f'{env_var}={os.environ[env_var]} la variable de entorno se ha creado con éxito.')

print('\n*** MUESTRA DIRECTORIO ACTUAL ***')
print(os.getcwd())
print(os.path.abspath('.'))
print(os.listdir('.'))

print('\n*** GENERA UN ERRROR SI NO ENCUENTRA UN FICHERO CONCRETO EN EL DIRECTORIO DE TRABAJO ***')
### ERROR AL ENCONTRAR UN FICHERO QUE NO ESTÁ EN EL DIRECTORIO DE TRABAJO ###
try:
    # Si el fichero buscado no se encuentra entonces lanza un IOError
    filename = input('Introduce el nombre del fichero que quieres ver: ')
    archivo = open(filename, 'r')
    texto = archivo.read()
    archivo.close()
    print(texto)

# El control salta aquí si alguna de las lineas anteriores lanza un IOError.
except IOError:
    print(os.error)
    print('ARCHIVO NO ENCONTRADO: ' + filename)

# Y en cualquiera de los casos la ejecución del código continua después del try/except
