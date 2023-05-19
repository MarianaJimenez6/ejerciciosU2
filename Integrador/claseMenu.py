from manejadorAlumnos import ManejadorAlumno as ManejadorAl
from manejadorMaterias import ManejadorMaterias as ManejadorMat

class Menu:
    __op = 0

    def __init__ (self,op = 0):
        self.__op = 0

    def item1(self, materias):
        dni = input("Ingrese el DNI de un alumno para informar su promedio con y sin aplazos: ")
        materias.promedio(dni)
            
    def item2(self, alumnos,materias):
        materia = input("Ingrese una materia para informar los estudiantes que la promocionaron: ")
        materias.buscarMateria(alumnos,materia)

    def item3(self, alumnos):
        print("item 3")
        alumnos.ordenar()
        alumnos.mostrarDatos()

    def mostrarMenu(self, alumnos,materias):
        if type(alumnos) == ManejadorAl:
            if type(materias) == ManejadorMat:
                band = False
                print('------Menu de opciones------')
                while not band:
                    print('\n')
                    print('1- Leer por teclado el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos.') 
                    print('2- Leer por teclado el nombre de una materia, e informar los estudiantes que la aprobaron en forma promocional, con nota mayor o igual que 7.')
                    print('3- Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre (ambos de menor a mayor).')
                    print('4- Salir')
                    self.__op = int(input('Seleccione una opcion: '))

                    if self.__op == 1:
                        print("hola")
                        self.item1(materias)

                    if self.__op == 2:
                        print("ghosla")
                        self.item2(alumnos,materias)

                    if self.__op == 3:
                        print("3")
                        self.item3(alumnos)

                    if self.__op == 4:
                        band = True
                        print('//////Menu cerrado//////')
                    self.__op = int(input('Seleccione una opcion: '))