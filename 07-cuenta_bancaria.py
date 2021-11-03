from clases.cuenta_bancaria import *

miCuenta = Cuenta('Harry Python', 0.00, '1234', '0000', True)


def login(cuenta):
    numero = input('\nIntroduce el Número de cuenta: ')
    clave = input('Introduce tu clave: ')

    if cuenta.numero == numero and cuenta.clave == clave:
        if cuenta.estado:
            print('** Acceso autorizado **')
            return True
        else:
            print('La cuenta está cerrada')
            return False
    else:
        print('\n** El número de cuenta o la clave introducidos son incorrectos **')
        return False


def operaciones(cuenta):
    inicio = True
    acceso = login(cuenta)
    if acceso:
        while inicio:
            print('\n>>> Bienvenido ' + cuenta.nombre + ' <<<\nEscribe la acción que deseas realizar:')
            opcion = input('\n1.Sacar dinero\n2.Ingresar dinero\n3.Consulta de saldo\n4.Salir\nTu opción: ')
            if opcion == '1':
                importe = input('\n¿Qué importe deseas sacar?: ')
                cuenta.sacarDinero(float(importe))
            elif opcion == '2':
                importe = input('\n¿Qué importe deseas ingresar?: ')
                cuenta.ingresarDinero(float(importe))
            elif opcion == '3':
                cuenta.getDatos()
            elif opcion == '4':
                inicio = False


### INICIO DEL PROGRAMA ###

inicio = True
while inicio:
    print('\n\n** Bienvenido al cajero de ZeroBank **\n\n¿Qué deseas hacer?:')
    opcion = input('\n1.Operar\n2.Salir\nTu opción: ')

    if opcion == '1':
        operaciones(miCuenta)
    elif opcion == '2':
        inicio = False
