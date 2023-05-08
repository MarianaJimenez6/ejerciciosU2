'''Ejercicio 6
Sobrecarga de operadores
Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:
1- Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).
2- Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.
3- Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.'''

from claseViajeroFrecuente import ViajeroFrecuente as Viajero
import csv 
from ManejadorViajeros import ManejadorViajeros

if __name__ == '__main__':
  viajeros = ManejadorViajeros()
  viajeros.cargarDatos()
  
  print("Lista de viajeros:")
  print("Numero de viajero, DNI, Nombre, Apellido y Millas acumuladas del viajero: ")
  viajeros.MostrarViajeros()
  
  print("Dirección de la lista de viajeros: ")
  print(viajeros.direcciones())
  
  print("--------------------------- Menú de opciones ---------------------------")
  print("1- Determinar el/los viajero/s con mayor cantidad de millas acumuladas. ")
  print("2- Acumular Millas                                                      ")
  print("3- Canjear Millas                                                       ")
  print("4- Salir                                                                ")
  print("------------------------------------------------------------------------")
  op = int(input("Seleccione una opción del menú: "))
  while op != 4:
    num = int(input("Ingrese número del viajero: "))
    rta = viajeros.Buscar(num)
    if rta != None:
      viajeros.Opciones(num,op)
    print("--------------------------- Menú de opciones ---------------------------")
    print("1- Determinar el/los viajero/s con mayor cantidad de millas acumuladas. ")
    print("2- Acumular Millas                                                      ")
    print("3- Canjear Millas                                                       ")
    print("4- Salir                                                                ")
    print("------------------------------------------------------------------------")
    op = int(input("Seleccione una opción del menú: "))