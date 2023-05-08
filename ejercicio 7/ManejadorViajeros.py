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
        entero = int(input("Ingrese un entero para comparar con la cantidad de millas del/a viajero/a "))
        if entero  == self.__listaViajeros[num-1].cantidadTotaldeMillas():
          print("El numero ingresado coincide con la cantidad de millas del/a viajero/a",self.__listaViajeros[num-1].getNom())
        else:
          print("El numero no coincide con las millas de ",self.__listaViajeros[num-1].getNom())
      elif op == 2:
        nuev_millas = int(input("Ingrese cantidad de millas a acumular: "))
        millas =  nuev_millas + self.__listaViajeros[num-1].cantidadTotaldeMillas()
        self.__listaViajeros[num-1].cantidadTotaldeMillas() = millas
        print("Cantidad de millas actualizada: ",self.__listaViajeros[num-1].cantidadTotaldeMillas())
      else:
        canje = int(input("Cantidad de millas a canjear: "))
        if canje <= self.__listaViajeros[num-1].cantidadTotaldeMillas():
          self.__listaViajeros[num-1] =  canje - self.__listaViajeros[num-1]
          print("Canje de millas exitoso. Cantidad de millas actual: ",self.__listaViajeros[num-1].cantidadTotaldeMillas())
        else:
          print("Error: Cantidad de millas insuficientes para canjear ")