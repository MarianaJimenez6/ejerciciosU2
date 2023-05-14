from claseConjunto import Conjunto

class Menu:
    __op = 0
    
    def __init__(self,op = 0):
        self.__op = op
    
    def item1(self, A,B):
        C = A+B
        print("\n Conjunto C : ",C)
        return
    
    def item2(self, A,B):
        C = A-B
        print("\n Conjunto C: A-B: ",C)
        return
    
    def item3(self, A,B):
        if A == B: 
            print("\nLos conjuntos A y B son iguales\n")
        else: 
            print("\nLos conjuntos A y B no son iguales\n")
        return
    
    def mostrarMenu(self, conjunto1,conjunto2):
        if type(conjunto1) == Conjunto:
            band = False
            print('------Menu de opciones------')
            while not band:
                print('\n')
                print('1- Unir dos conjuntos ')
                print('2- Mostrar la diferencia entre dos conjuntos')
                print('3- Comparar los conjuntos y verificar si son iguales')
                print('4- Salir')
    
                if self.__op == 1:
                    self.item1(conjunto1,conjunto2)
    
                if self.__op == 2:
                    self.item2(conjunto1,conjunto2)
    
                if self.__op == 3:
                    self.item3(conjunto1,conjunto2)
    
                if self.__op == 4:
                    band = True
                    print('//////Menu cerrado//////')
                self.__op = int(input('Seleccione una opcion: '))
