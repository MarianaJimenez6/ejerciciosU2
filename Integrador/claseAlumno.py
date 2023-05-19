class Alumno:
   __DNI = None
   __apellido = None
   __nombre = None
   __carrera = None
   __año_que_cursa = None
   
   def __init__(self,dni,ap,nom,carrera,año):
      self.__DNI = dni
      self.__apellido = ap
      self.__nombre = nom
      self.__carrera = carrera
      self.__año_que_cursa = año
   
   def getDNI(self):
      return self.__DNI
   
   def getApellido(self):
      return self.__apellido
   
   def getNombre(self):
      return self.__nombre
   
   def getNombreYApellido(self):
      s = ''
      s += str(self.__nombre)+","+str(self.__apellido)
   
   def getCarrera(self):
      return self.__carrera
   
   def getAnio(self):
      self.__año_que_cursa
   
   def mostrar(self):
      print('DNI {}, Apellido {}, Nombre {}, Carrera {}, Año que cursa {}'.format(self.__DNI, self.__apellido, self.__nombre, 
      self.__carrera, self.__año_que_cursa))
   
   def __gt__(self,otro):
      if type(otro) == str:
         return self.__apellido > otro
      else:
         return self.__año_que_cursa > otro
