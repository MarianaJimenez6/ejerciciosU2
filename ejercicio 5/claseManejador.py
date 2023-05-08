import csv
from claseplan import PlanAhorro

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def addPlan(self, plan1):
        if type(plan1) == PlanAhorro:
            self.__lista.append(plan1)

    def __str__(self):
        s = ''
        for planAhorro in self.__lista:
            s += str(planAhorro) + '\n\n'
        return s

    def CargaLista(self): 
        band = True
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            plan1 = PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3]))
            self.addPlan(plan1)
        archivo.close()

    def calculoCuota(self):
        i = 0
        while i < len(self.__lista):
            self.__lista[i].calculoCuota()
            i += 1  

    def actualizarimporte(self):
        i = 0
        while i < len(self.__lista):
            print('\nCodigo de plan: {}, Modelo: {},Version del Vehiculo: {},Importe: {}'.format(self.__lista[i].getCodigoPlan(),self.__lista[i].getModeloVehiculo(),self.__lista[i].getVersionVehiculo(),self.__lista[i].getValorVehiculo()))
            old_valor = float(input('Ingrese el valor actual del vehiculo: '))
            self.__lista[i].actualizacionValor(old_valor)

    def mostrarDatos(self,valor1):
        if type(valor1) == float:
            i = 0
            while i < len(self.__lista):
                if self.__lista[i].getValorCuota < valor1:
                    print('\nCodigo de plan: {},Modelo: {},Version del Vehiculo: {}'.format(self.__lista[i].getCodigoPlan(),self.__lista[i].getModeloVehiculo(),self.__lista[i].getVersionVehiculo()))
                    i += 1
                else:
                    i += 1 

    def mostrarPago(self):
        codigoPlan = int(input('Indique el codigo de un plan'))
        i = 0
        band = False
        while i < len(self.__lista) and not band:
            if(self.__lista[i].getCodigoPlan) == codigoPlan:
                licitar_valor = (PlanAhorro.CantCuotas()) * self.__lista[i].getValorCuota()
                print('\nLa cuota que se debe abonar para licitar el vehiculo {} es de {}'.format(self.__lista[i].getModeloVehiculo(), licitar_valor))
                band = True
            else:
                i += 1
            if not band:
                print('El plan no se encontró')





