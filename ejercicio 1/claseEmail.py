class Email:
  __idCuenta = None
  __dominio = None
  __tipoDominio = None
  __contra = None
  
  def __init__ (self,idCuenta,dom,tipo,contra):
    self.__idCuenta = idCuenta
    self.__dominio = dom
    self.__tipoDominio = tipo
    self.__contra = contra
  
  def retornaEmail (self):
    return (self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDominio)
  
  def getDominio (self):
    return self.__dominio
  
  def getIdCuenta(self):
    return self.__idCuenta
  
  def getContra(self):
    return self.__contra
  
  def CrearCuenta(self,email): 
    cadena = Email.split("@")
    self.__idCuenta = cadena[0]
    cadena2 = cadena[1].split(".")
    self.__dominio = cadena2[0]
    self.__tipoDominio = cadena2[1]
    cadena3 = cadena2[1].split(",")
    self.__contra = cadena3[0]
