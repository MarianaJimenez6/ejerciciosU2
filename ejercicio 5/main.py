'''Ejercicio 5
Datos miembro estáticos y Funciones miembro estáticas 
Un concesionario de automóviles ofrece distintos planes de ahorro y se requiere la definición de una clase “PlanAhorro” que represente a cada uno de ellos.
Los datos que es necesario registrar son: código del plan, modelo y versión del vehículo, valor del vehículo, cantidad de cuotas del plan, cantidad de cuotas que debe tener pagas para licitar el vehículo (los últimos dos atributos son los mismos para todos los planes).
El primer día hábil del mes se actualiza el valor del vehículo.
El importe de la cuota se calcula:
valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.10
Implemente un programa que: 
1- Lea desde un archivo separado con “;” los datos de los planes y genere una lista que almacene instancias de la clase “PlanAhorro”.
2- Presente un menú de opciones permita:
a. Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.
b. Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.
c. Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).
d. Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.
'''

from claseplan import PlanAhorro
from claseManejador import Manejador
from menuplan import Menu

def test():
    print('Testeando')
    plan1= PlanAhorro(1,"Gol 2010","Version 1",200000)
    print('\n///antes de calcular la cuota///')
    print(plan1)
    plan1.calculoCuota()
    print('\n///despues del calculo de la cuota///')
    print(plan1)
    plan1.actualizacionValor(float(2000))
    plan1.actualizacionValor(float(plan1.getValorVehiculo()))
    print('\nValor del vehiculo actualizado: ')
    print(plan1)
    print('fin del test')

if __name__ == '__main__':
    test()
    manejador1 = Manejador()
    menu1 = Menu()
    manejador1.CargaLista()
    manejador1.calculoCuota()
    print(manejador1)
    menu1.mostrarMenu(manejador1)
