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
  
  def CantidadTotaldeMillas(self):
    return self.__millas_acum
  
  def getViajeros(self):
    return (self.__num_viajero, self.__DNI, self.__nombre, self.__apellido, self.__millas_acum)
  
  def AcumularMillas(self,millas_recorridas):
    self.__millas_acum = self.__millas_acum + millas_recorridas
    print("Cantidad de millas actualizada: ",self.__millas_acum) 
  
  def CanjearMillas(self,millas_canjear):
    if millas_canjear <= self.__millas_acum:
      self.__millas_acum = self.__millas_acum - millas_canjear
      print("Canje de millas exitoso. Cantidad de millas actual: ",self.__millas_acum)
    else:
      print("Error: Cantidad de millas insuficientes para canjear ") 