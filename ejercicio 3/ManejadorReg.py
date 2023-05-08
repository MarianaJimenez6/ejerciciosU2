from claseRegistro import Registro
import csv

class ManejadorRegistro:
  __listaReg = []
  def __init__(self):
    self.__listaReg = []
    for i in range(30):
      self.__listaReg.append([])
      for j in range(24):
        self.__listaReg[i].append(None)
    #print(self.__listaReg[29][23])
  
  def cargarDatos(self):
    archivo = open('ArchivoRegMeteorologico.csv')
    reader = csv.reader(archivo,delimiter=",")
    band = True
    for fila in reader:
      if band:
        band = not band #saltea cabecera
      else:
        dia = int(fila[0])
        hora = int(fila[1])
        temperatura = fila[2]
        humedad = fila[3]
        presion_atmos = fila[4]
        registro = Registro(temperatura,humedad,presion_atmos)
        self.agregarRegistro(dia, hora, registro)
    archivo.close()

  def mostrarRegistro(self, dia, hora):
    print(self.__listaReg[dia-1][hora])

  def agregarRegistro(self, dia, hora, registro):
    self.__listaReg[dia-1][hora] = registro
  
  def mostrarMayorYMenor(self): #inciso 1
    minTemperatura = 999
    diaTempMin = None
    horaTempMin = None
    maxTemperatura = -999
    diaTempMax = None
    horaTempMax = None
    minHumedad = 999
    diaHumMin = None
    horaHumMin = None
    maxHumedad = -999
    diaHumMax = None
    horaHumMax = None
    minPresion = 999
    diaPresMin = None
    horaPresMin = None
    maxPresion = -999
    diaPresMax = None
    horaPresMax = None

    for i in range(len(self.__listaReg)):
      for j in range(len(self.__listaReg[i])):
        if type(self.__listaReg[i][j]) == Registro:
          temperatura = self.__listaReg[i][j].getTemperatura()
          humedad = self.__listaReg[i][j].getHumedad()
          presion = self.__listaReg[i][j].getPresion()
          if temperatura < minTemperatura:
            minTemperatura = temperatura
            diaTempMin = i + 1
            horaTempMin = j
          if temperatura > maxTemperatura:
            maxTemperatura = temperatura
            diaTempMax = i + 1
            horaTempMax = j
          if humedad < minHumedad:
            minHumedad = humedad
            diaHumMin = i + 1
            horaHumMin = j
          if humedad > maxHumedad:
            maxHumedad = humedad
            diaHumMax = i + 1
            horaHumMax = j
          if presion < minPresion:
            minPresion = presion
            diaPresMin = i + 1
            horaPresMin = j
          if presion > maxPresion:
            maxPresion = presion
            diaPresMax = i + 1
            horaPresMax = j

    print("La temperatura máxima fue de: {} y se registro el día {} a las {} hs".format(maxTemperatura,
                                                                                        diaTempMax,
                                                                                        horaTempMax))
    print("La temperatura mínima fue de: {} y se registro el día {} a las {} hs".format(minTemperatura,
                                                                                        diaTempMin,
                                                                                        horaTempMin))
    print("La humedad máxima fue de: {} y se registro el día {} a las {} hs".format(maxHumedad,
                                                                                        diaHumMax,
                                                                                        horaHumMax))
    print("La humedad mínima fue de: {} y se registro el día {} a las {} hs".format(minHumedad,
                                                                                        diaHumMin,
                                                                                        horaHumMin))
    print("La presión máxima fue de: {} y se registro el día {} a las {} hs".format(maxPresion,
                                                                                        diaPresMax,
                                                                                        horaPresMax))
    print("La presión mínima fue de: {} y se registro el día {} a las {} hs".format(minPresion,
                                                                                        diaPresMin,
                                                                                        horaPresMin))
  
  def temperaturaPromedio(self): #inciso 2
    suma = []
    cant = []
    for i in range(24):
      suma.append(0)
      cant.append(0)
    
    for i in range(len(self.__listaReg)):
      for j in range(len(self.__listaReg[i])):
        if (type(self.__listaReg[i][j]) == Registro):
          temp = self.__listaReg[i][j].getTemperatura()
          suma[j] += temp
          cant[j] += 1
          
    for i in range(len(suma)):
      suma[i] = suma[i] / cant[i]
      print("La temperatura promedio a las {} hs es de {} grado".format(i, suma[i]))
  
  def listar(self,dia): #inciso 3 
    for i in range (len(self.__listaReg[dia-1])):
      if type(self.__listaReg[dia][i]) == Registro:
        print("Hora:" ,i,self.__listaReg[dia-1][i])
