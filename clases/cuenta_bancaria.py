class Cuenta:
    def __init__(self, nombre, saldo, numero, clave, estado):
        self.nombre = nombre
        self.saldo = saldo
        self.numero = numero
        self.clave = clave
        self.estado = estado

    def sacarDinero(self, importeSacado):
        if importeSacado <= self.saldo:
            self.saldo -= importeSacado
            print('Operación de salida de ' + str(importeSacado) + '€ realizada con éxito')
        else:
            print('** Saldo insuficiente, tu saldo actual es: ' + str(self.saldo) + ' **\n')

    def ingresarDinero(self, importeIngresado):
        self.saldo += importeIngresado
        print('Operación de ingreso de ' + str(importeIngresado) + '€ realizada con éxito')

    def getDatos(self):
        print('''
        Nombre: ''' + self.nombre + '''
        Número de cuenta: ''' + self.numero + '''
        Saldo: ''' + str(self.saldo) + '''+ 
        Estado: ''' + str(self.estado) + '''
        ''')
