class Ventana:
  __titulo = None
  __x_sup_izq = None
  __y_sup_izq = None
  __x_inf_der = None
  __y_inf_der = None
  
  def __init__(self,titulo,x_sup = 0,y_sup = 0,x_inf = 500,y_inf = 500):
    self.__titulo = titulo
    self.__x_sup_izq = x_sup
    self.__y_sup_izq = y_sup
    self.__x_inf_der = x_inf
    self.__y_inf_der = y_inf

  def getTitulo(self):
    return self.__titulo
  
  def alto(self):
    return print(self.__y_sup_izq  ,"x", self.__y_inf_der)

  def ancho(self):
    return print(self.__x_sup_izq ,"x", self.__x_inf_der)

  def mostrar(self):
    return print("superior izquierdo x: {}, superior derecho y: {}, inferior derecho x: {}, inferior derecho y: {}".format(self.__x_sup_izq,self.__y_sup_izq,self.__x_inf_der,self.__y_inf_der))

  def moverDerecha(self,unidades = 1):
    if self.__x_sup_izq < self.__x_inf_der:
      self.__x_sup_izq += unidades
      self.__x_inf_der += unidades
    else:
      print("el valor de la x superior izquierda debe ser menor al de la inferior derecha para realizar la operación")

  def moverIzquierda(self,unidades = 1):
    if self.__x_sup_izq < self.__x_inf_der:
      self.__x_sup_izq -= unidades
      self.__x_inf_der -= unidades
    else:
      print("el valor de la x superior izquierda debe ser menor al de la inferior derecha para realizar la operación")

  def bajar(self,unidades = 1):
    if self.__y_sup_izq < self.__y_inf_der:
      self.__y_sup_izq -= unidades
      self.__y_inf_der -= unidades
    else:
      print("el valor de la y superior izquierda debe ser menor al de la inferior derecha para realizar la operación")


  def subir(self,unidades = 1):
    if self.__y_sup_izq < self.__y_inf_der:
      self.__y_sup_izq += unidades
      self.__y_inf_der += unidades
    else:
      print("el valor de la y superior izquierda debe ser menor al de la inferior derecha para realizar la operación")
