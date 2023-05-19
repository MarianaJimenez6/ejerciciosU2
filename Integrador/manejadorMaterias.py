from claseMateriasAprobadas import Materia_Aprobada as Materia
import csv

class ManejadorMaterias:
  __listaMaterias = []

  def __init__(self):
    self.__listaMaterias = []
  
  def cargarDatos(self):
    archivo = open('materiasAprobadas.csv')
    reader = csv.reader(archivo,delimiter=";")
    band = True
    for fila in reader:
      if band:
        band = not band #saltea cabecera
      else:
        dni = fila[0]
        materia = fila[1]
        fecha = fila[2]
        nota = [3]
        aprobacion = fila[4]
        materiaAprobada1 = Materia(dni,materia,fecha,nota,aprobacion)
        self.agregarMateria(materiaAprobada1)
    archivo.close()
  
  def agregarMateria(self,unaMateria):
    self.__listaMaterias.append(unaMateria)

  def mostrarDatos(self):
    i = 0
    for i in range(len(self.__listaMaterias)):
      print(self.__listaMaterias[i].mostrar())

  def promedio(self,dni):
    i = 0
    promedioAplazo = 0
    promedioSinAplazo = 0
    cantidadApl = 0
    cantidadSinApl = 0
    while i < len(self.__listaMaterias):
      if self.__listaMaterias[i].getDNI() == dni:
        nota = self.__listaMaterias[i].getNota()
        print("Materia: {}, Nota: {}".format(self.__listaMaterias[i].getMateria(),nota))
        if self.__listaMaterias[i].getNota() > 4:        
          promedioSinAplazo = promedioSinAplazo + nota
          cantidadSinApl = cantidadSinApl + 1
          i = i + 1
        else:
          promedioAplazo = promedioAplazo + nota
          cantidadApl = cantidadApl + 1
          i = i + 1
      else:
        i = i + 1
    promedioAplazo = (promedioAplazo + promedioSinAplazo)/(cantidadApl + cantidadSinApl)
    print("Promedio con aplazos:" .format(promedioAplazo))
    promedioSinAplazo = promedioSinAplazo / cantidadSinApl
    print("Promedio sin aplazos:" .format(promedioSinAplazo))

  def buscarMateria(self,arreglo,materia):
    i = 0
    lista_dni = []
    while i < (len(self.__listaMaterias)):
      notas = self.__listaMaterias[i].getNota() 
      if (self.__listaMaterias[i].getMateria() == materia and self.__listaMaterias[i].getAprobacion() == 'P'and notas > 6):
        d = 'DNI'
        a = 'Apellido y nombre'
        f = 'fecha'
        nota = 'Nota'
        año = 'Año que cursa'
        print("{:15^}{:15^}{:15^}{:15^}{:15^}".format(d,a,f,nota,año))
        dni = self.__listaMaterias[i].getDNI()
        fecha = self.__listaMaterias[i].getFecha()
        NyA = arreglo.buscarNyA(self.__listaMaterias[i].getDNI())
        nota = self.__listaMaterias[i].getNota()
        año_que_cursa = arreglo.buscarAnio(self.__listaMaterias[i].getDNI())
        i = i+1
      else:
        i = i+1

  def __str__(self):
    s = ''
    for materia in self.__listaMaterias:
      s = s+ str(materia) + "\n"
    return s

