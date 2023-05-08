class ViajeroFrecuente:
  __num_viajero = int
  __DNI = str
  __nombre = str
  __apellido = str
  __millas_acum = int
  
  def __init__(self,num,dni,nom,ap,millas):
    self.__num_viajero = int(num)
    self.__DNI = dni
    self.__nombre = nom
    self.__apellido = ap
    self.__millas_acum = int(millas)
  
  def getNum(self):
    return self.__num_viajero
  
  def getDNI(self):
    return self.__DNI
  
  def getNom(self):
    return self.__nombre
  
  def getAp(self):
    return self.__apellido
  
  def cantidadTotaldeMillas(self):
    return self.__millas_acum
  
  def getViajeros(self):
    return (self.__num_viajero, self.__DNI, self.__nombre, self.__apellido, self.__millas_acum)
  
  def __req__(self,otro): #ejercicio 7
    compara = self.__millas_acum > otro.cantidadTotaldeMillas()
    return compara
  
  def __radd__(self,millas_recorridas): #ejercicio 7
    acum = self.__millas_acum + millas_recorridas
    return acum
  
  def __rsub__(self,millas_canjear): #ejercicio 7
    resta = self.__millas_acum - millas_canjear
    return resta
