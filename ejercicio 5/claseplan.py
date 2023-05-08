class PlanAhorro:
    __cod_Plan = None
    __modelo = None
    __versionVehiculo = None
    __valorVehiculo = None
    __ValorCuota = None
    CantCuotas = 84
    CuotasNecesarias = 15

    def __init__(self, codigo = None, modelo = None, version = None, valor= None, ValorCuota = 0):
        self.__cod_Plan = codigo
        self.__modelo = modelo
        self.__versionVehiculo = version
        self.__valorVehiculo = valor
        self.__ValorCuota = ValorCuota

    def getCodigoPlan(self):
        return self.__cod_Plan

    def getValorVehiculo(self):
        return self.__valorVehiculo

    def getVersionVehiculo(self):
        return self.__versionVehiculo

    def getModeloVehiculo(self):
        return self.__modelo

    def actualizacionValor(self,valor_actual):
        if type(valor_actual) == float:
            if self.__valorVehiculo == valor_actual:
                nuev_valor = float(input('Ingrese el nuevo valor del vehículo: '))
                self.__valorVehiculo = nuev_valor
            else:
                print('valor erroneo')

    def calculoCuota(self):
        cuota = (self.__valorVehiculo/ PlanAhorro.getcantCuotas()) + (self.__valorVehiculo * 0.10)
        self.__ValorCuota = cuota

    def getValorCuota(self):
        return self.__ValorCuota

    def __str__(self):
        return 'Codigo de plan: {}\nModelo del vehiculo: {}\nVersion del vehiculo: {}\nImporte total: {}\nImporte de la cuota: {}\n'.format(self.__cod_Plan,self.__modelo,self.__versionVehiculo,self.__valorVehiculo,self.__ValorCuota)

    @classmethod
    def getcantCuotas(cls):
        return cls.CantCuotas

    def setcantCuotas(cls,cantidad):
        cls.CantCuotas = cantidad

    def setcantCuotasNecesarias(cls,cantidad):
        cls.CuotasNecesarias = cantidad