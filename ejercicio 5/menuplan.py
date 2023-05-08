from claseplan import PlanAhorro
from claseManejador import Manejador

class Menu:
    __op = 0

    def __init__(self, op=0):
        self.__op = op

    def item1(self, manejador1):
        if type(manejador1) == Manejador:
            manejador1.actualizarimporte()
            print(manejador1)

    def item2(self, manejador1):
        if type(manejador1) == Manejador:
            nuev_valor = float(input('Ingrese un numero de plan: '))
            manejador1.mostrarDatos(nuev_valor)

    def item3(self, manejador1):
        if type(manejador1) == Manejador:
            manejador1.mostrarPago()

    def item4(self):
        cant = int(input('Ingrese el numero de cuotas nuevo: '))
        PlanAhorro.setcantCuotas(cant)

    def mostrarMenu(self, manejador1):
        if type(manejador1) == Manejador:
            band = False
            print('//////Menu de opciones//////')
            print('\n')
            print('1- Actualizar para cada plan el importe de los vehiculos ')
            print('2- Para un plan ingresado por teclado, mostrar datos de un plan con importe inferior al ingresado')
            print('3- Consultar por licitación de un vehiculo')
            print('4- Modificar la licitación de todos los planes')
            print('5- Salir')
            while not band:
                if self.__op == 1:
                    self.item1(manejador1)
                if self.__op == 2:
                    self.item2(manejador1)
                if self.__op == 3:
                    self.item3(manejador1)
                if self.__op == 4:
                    self.item4(manejador1)
                if self.__op == 5:
                    band = True
                    print('//////Menu cerrado//////')
                else:
                    print('Opcion Incorrecta')
                    input('ENTER para continuar: ')
                print('\n')
                print('1- Actualizar para cada plan el importe de los vehiculos ')
                print('2- Para un plan ingresado por teclado, mostrar datos de un plan con importe inferior al ingresado')
                print('3- Consultar por licitación de un vehiculo')
                print('4- Modificar la licitación de todos los planes')
                print('5- Salir')
                self.__op = int(input('Seleccione una opcion: '))