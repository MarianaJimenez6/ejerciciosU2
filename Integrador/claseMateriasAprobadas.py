class Materia_Aprobada:
     __DNI = None
     __nombre_materia = None
     __fecha = None
     __nota = None
     __aprobacion = None
     
     def __init__(self,dni,nom_materia,fecha,nota,aprobacion):
          self.__DNI = dni
          self.__nombre_materia = nom_materia
          self.__fecha = fecha
          self.__nota = nota
          self.__aprobacion = aprobacion
     
     def getDNI(self):
          return self.__DNI
     
     def getMateria(self):
          return self.__nombre_materia
     
     def getFecha(self):
          return self.__fecha
     
     def getNota(self):
          return self.__nota
     
     def getAprobacion(self):
          return self.__aprobacion
     
     def mostrar(self):
          print('DNI {}, materia {}, fecha {}, nota {}, aprobacion {}'.format(self.__DNI, self.__nombre_materia, self.__fecha, 
          self.__nota,self.__aprobacion))
     