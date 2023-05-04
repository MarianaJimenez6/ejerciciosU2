'''Ejercicio 2
Listas
En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de puntos.
Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el diseño de clase.
Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
Métodos:
a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.
Implemente un programa que:
1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.
2- El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con las siguientes opciones:
a- Consultar Cantidad de Millas.
b- Acumular Millas.
c- Canjear Millas.
3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.
4.1- El usuario elige la opción Acumular Millas, el sistema solicita el número de viajero frecuente y la cantidad de millas, el sistema busca el viajero, si lo encuentra acumula las millas ingresadas, e informa el nuevo total de millas acumulada; si el sistema no encuentra el viajero frecuente, informa al usuario de tal situación.
4.2- El usuario elige la opción Canjear Millas, el sistema solicita el número de viajero frecuente y la cantidad de millas a canjear, el usuario ingresa número de viajero frecuente y cantidad de millas a canjear, el sistema busca el viajero frecuente, si lo encuentra, verifica que la cantidad de millas acumuladas alcancen  para el canje, si no alcanzan informa la situación al usuario, si alcanzan hace el canje e informa al usuario que pudo realizar el canje y muestra la nueva cantidad de millas acumuladas; si el viajero frecuente no existe, el sistema informa al usuario de tal situación.'''

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
  
  print("------- Menú de opciones -------")
  print("1- Consultar Cantidad de Millas ")
  print("2- Acumular Millas              ")
  print("3- Canjear Millas               ")
  print("4- Salir                        ")
  print("--------------------------------")
  op = int(input("Seleccione una opción del menú: "))
  while op != 4:
    num = int(input("Ingrese número del viajero: "))
    rta = viajeros.Buscar(num)
    if rta != None:
      viajeros.Opciones(num,op)
    print("------- Menú de opciones -------")
    print("1- Consultar Cantidad de Millas ")
    print("2- Acumular Millas              ")
    print("3- Canjear Millas               ")
    print("4- Salir                        ")
    print("--------------------------------")
    op = int(input("Seleccione una opción del menú: "))