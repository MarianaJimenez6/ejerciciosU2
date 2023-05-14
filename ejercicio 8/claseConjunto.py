class Conjunto:
  __lista = []
  
  def __init__(self):
    self.__lista = []

  def cargaLista(self):
    num = int(input("Nuevo número para la lista, termine con -1: "))
    while num != -1:
      self.__lista.append(num)
      num = int(input("Nuevo número para la lista, termine con -1: "))

  def __str__(self):
    return "%s" %(self.__lista)

  def __add__(self,otro):
    lista2 = []
    self.__lista.sort()
    otro.__lista.sort()
    a = len(self.__lista)
    b = len(otro.__lista)
    i = 0
    j = 0
    while i < a and j < b:
      if self.__lista[i] < otro.__lista[j]:
        lista2.append(self.__lista[i])
        i = i+1
      elif self.__lista[i] == otro.__lista[j]:
        lista2.append(otro.__lista[j])
        i = i+1
        j = j+1
      else:
        lista2.append(self.__lista[i])
        i = i+1
        j = j+1
    if i<a:
      while i<a:
        lista2.append(self.__lista[i])
        i = i+1
    if j<b:
      while j<b:
        lista2.append(otro.__lista[j])
        j = j+1
    return lista2

  def __sub__(self,otro):
    conjunto_resultante = []
    self.__lista.sort()
    otro.__lista.sort()
    a = len(self.__lista)
    b = len(otro.__lista)
    i = 0
    j = 0
    band = False
    while i < a:
      band = False
      while j < b and band == False:
        if self.__lista[i] == otro.__lista[j]:
          band = True
        else:
          j = j+1
      if band == False:
        conjunto_resultante.append(self.__lista[i])
        i = i+1
        j = 0
      else:
        i = i+1
        j = 0
    return conjunto_resultante

  def __eq__(self,otro):
    self.__lista.sort()
    otro.__lista.sort()
    a = len(self.__lista)
    b = len(otro.__lista)
    band = None
    if a == b:
      i = 0
      band = True
      while i < a and band == True:
        if self.__lista[i] == otro.__lista[i]:
          i = i+1
        else:
          band = False
    else:
      band = False
    return band  