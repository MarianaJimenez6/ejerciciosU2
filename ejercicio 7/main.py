'''Ejercicio 7
Sobrecarga por derecha (reverse operators)
Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:
1- Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.
2- Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.
3- Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.'''

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
  
  print("------------------------------------ Menú de opciones ------------------------------------")
  print("1- Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero ")
  print("2- Acumular Millas                                                                        ")
  print("3- Canjear Millas                                                                         ")
  print("4- Salir                                                                                  ")
  print("------------------------------------------------------------------------------------------")
  op = int(input("Seleccione una opción del menú: "))
  while op != 4:
    num = int(input("Ingrese número del viajero: "))
    rta = viajeros.Buscar(num)
    if rta != None:
      viajeros.Opciones(num,op)
    print("------------------------------------ Menú de opciones ------------------------------------")
    print("1- Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero ")
    print("2- Acumular Millas                                                                        ")
    print("3- Canjear Millas                                                                         ")
    print("4- Salir                                                                                  ")
    print("------------------------------------------------------------------------------------------")
    op = int(input("Seleccione una opción del menú: "))