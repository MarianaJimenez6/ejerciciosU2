import numpy as np
from claseAlumno import Alumno
import csv

class ManejadorAlumno:
    __cantidad = 0
    __dimension = 0
    __incremento = 0
    __alumnos = None
    
    def __init__(self,dimension,cantidad = 0,incremento = 5):
        self.__alumnos = np.empty(dimension, dtype=Alumno)
        self.__dimension = dimension
        self.__cantidad = cantidad
        self.__incremento = incremento
    
    def agregarAlumno(self, alumno):
        if self.__cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__alumnos.resize(self.__dimension)
        else: 
            self.__alumnos[self.__cantidad] = alumno
            self.__cantidad =self.__cantidad + 1
    
    def cargarDatos(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo,delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = not band #saltea cabecera
            else:
                DNI = fila[0]
                apellido = fila[1]
                nombre = fila[2]
                carrera = fila[3]
                año_que_cursa = fila[4]
                alumno1= Alumno(DNI,apellido,nombre,carrera,año_que_cursa)
                self.agregarAlumno(alumno1)
        archivo.close()
    
    def mostrarDatos(self):
        cant = len(self.__alumnos)
        for i in range (len(self.__alumnos)):
            if type(self.__alumnos[i]) == Alumno:
                print("mostrar datos: ")
                print(self.__alumnos[i].mostrar())
    
    def ordenar(self): #ordenar bien jsjs
        # Se calcula la longitud del arreglo para tener un código más limpio
        longitud = self.__cantidad
        # Se recorre todo el arreglo
        for i in range(1,longitud):
            aux = self.__alumnos[i]
            valor = self.__alumnos[i].getApellido()
            j = i - 1
            # Dentro del ciclo, se lo vuelve a recorrer. Pero ahora hasta el penúltimo elemento
            while j >= 0 and self.__alumnos[j] > valor:
                self.__alumnos[j + 1] = self.__alumnos[j]
                j = j-1
            self.__alumnos[j + 1] = aux
        for i in range(1,longitud):
            aux = self.__alumnos[i]
            anio = int(self.__alumnos[i].getAnio())
            j = i-1
            while j >= 0 and self.__alumnos[j].getAnio() > anio:
                self.__alumnos[j+1] = self.__alumnos[j]
                j = j-1
            self.__alumnos[j+1] = aux
    
    
    def mostrarPromocionales(self,lista):
        i = 0
        for i in range(len(lista)):
            print(lista[i].mostrar())
    
    def buscarNyA(self,dni):
        i = 0
        band = False
        while i < self.__cantidad and band == False:
            if self.__alumnos[i].getDNI() == dni:
                nombreYApellido = self.__alumnos[i].getNombreYApellido()
                band = True
            else:
                i = i + 1
        return nombreYApellido
    
    def buscarAnio(self,dni):
        i = 0
        band = False
        anio = ''
        while i < self.__cantidad and band == False:
            if self.__alumnos[i].getDNI() == dni:
                anio = self.__alumnos[i].getAnio()
                band = True
                i = i+1
            else:
                i = i+1
        return anio

