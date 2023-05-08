class Registro:
  __temperatura = None
  __humedad = None
  __presion_atmos = None
  
  def __init__(self,temp,humedad,presion):
    self.__temperatura = float(temp)
    self.__humedad = int(humedad)
    self.__presion_atmos = int(presion)
  
  def __str__(self):
    return "Temperatura: {}, Humedad: {}, Presion: {}".format(self.__temperatura, self.__humedad, self.__presion_atmos)

  def getTemperatura(self):
    return self.__temperatura
  
  def getHumedad(self):
    return self.__humedad
  
  def getPresion(self):
    return self.__presion_atmos