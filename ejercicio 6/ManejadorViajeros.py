from claseViajeroFrecuente import ViajeroFrecuente as Viajero
import csv
class ManejadorViajeros:
  __listaViajeros = []
  def __init__ (self):
    __listaViajeros = []

  def cargarDatos(self):
    archivo = open('ArchivoViajerosF.csv')
    reader = csv.reader(archivo,delimiter=",")
    band = True
    for fila in reader:
      if band:
        band = not band #saltea cabecera
      else:
        num = fila[0]
        dni = fila[1]
        nom = fila[2]
        ap = fila[3]
        millas = fila[4]
        viajero = Viajero(num,dni,nom,ap,millas)
        self.AgregarViajero(viajero)
    archivo.close()
  
  def AgregarViajero(self,unViajero):
    self.__listaViajeros.append(unViajero)
  
  def MostrarViajeros(self): 
    i = 0
    for i in range (len(self.__listaViajeros)):
      print (self.__listaViajeros[i].getViajeros())
  
  def Buscar(self,num): #busca el numero de un viajero en la lista
    indice = 0
    ValorRetorno = None
    bandera = False
    while not bandera and indice < len(self.__listaViajeros):
      if self.__listaViajeros[indice].getNum() == num:
        ValorRetorno = indice
        bandera = True
      else:
        indice +=1
    return ValorRetorno
  
  def direcciones(self):
    i = 0
    print(hex(id(self.__listaViajeros)))
    for i in range (len(self.__listaViajeros)):
      print("Dirección de memoria del elemento de la lista n° ", i + 1 )
      print(id(i))
  
  def Opciones(self,num,op):
    if (op > 0) & (op < 4):
      if op == 1:
        i= 0
        max = 1
        for i in range (len(self.__listaViajeros)):
          if self.__listaViajeros[i].cantidadTotaldeMillas() > self.__listaViajeros[i+1].cantidadTotaldeMillas():
            max = self.__listaViajeros[i].cantidadTotaldeMillas()
          if self.__listaViajeros [i] == max:
            print("Viajero con más cantidad de millas: ",self.__listaViajeros[num-1].getNom(),": ",self.__listaViajeros[num-1].cantidadTotaldeMillas())
      elif op == 2:
        nuev_millas = int(input("Ingrese cantidad de millas a acumular: "))
        self.__listaViajeros[num-1] = self.__listaViajeros[num-1] + nuev_millas
        print("Cantidad de millas actualizada: ",self.__listaViajeros[num-1].cantidadTotaldeMillas())
      else:
        canje = int(input("Cantidad de millas a canjear: "))
        if canje <= self.__listaViajeros[num-1].cantidadTotaldeMillas():
          self.__listaViajeros[num-1] = self.__listaViajeros[num-1] - canje
          print("Canje de millas exitoso. Cantidad de millas actual: ",self.__listaViajeros[num-1].cantidadTotaldeMillas())
        else:
          print("Error: Cantidad de millas insuficientes para canjear ")