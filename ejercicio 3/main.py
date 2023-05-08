'''Ejercicio 3
Listas bidimensionales
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. 
Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: 
número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.
Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.
Implemente un programa que:
1. Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.
2. Almacene en la lista bidimensional los datos registrados en el archivo.
3. Presente un menú de opciones permita realizar las siguientes tareas:
3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
3.2. Indicar la temperatura promedio mensual por cada hora.
3.3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.'''

from claseRegistro import Registro
from ManejadorReg import ManejadorRegistro as Manejador

def menu(registros):
  
  salir = False

  while not salir:
    print("|------------------------------------Menu de opciones-------------------------------------------|")
    print("|1- Mostrar para cada variable, el día y hora de menor y mayor valor.                           |")
    print("|2- Indicar la temperatura promedio mensual por cada hora.                                      |")
    print("|3- Dado un número de día, listar los valores de las tres variables para cada hora del día dado.|")
    print("|4- Salir                                                                                       |")
    print("|-----------------------------------------------------------------------------------------------|")
    op = int(input("Elija una opción del menu: "))

    if op == 1:
      registros.mostrarMayorYMenor()    
    elif op == 2:
      registros.temperaturaPromedio()
    elif op == 3:
      dia = int(input("Ingrese el numero de dia del que requiera informe: "))
      registros.listar(dia)
    elif op == 4:
      salir = True
    else:
      print("Opción incorrecta.")

if __name__ == '__main__':
  registros = Manejador()
  registros.cargarDatos()
  #registros.mostrarRegistro(3, 23)
  menu(registros)