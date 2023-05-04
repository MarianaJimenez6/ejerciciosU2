from claseEmail import Email
class ManejadorEmails:
    __listaEmails = []
    def __init__(self):
        self.__listaEmails = []
    
    def agregarEmail(self,unEmail):
        self.__listaEmails.append(unEmail)
    
    #4 a
    def mostrarEmails(self):
        for i in range (len(self.__listaEmails)):
            print(self.__listaEmails[i].retornaEmail()) 
            print(self.__listaEmails[i].getContra())
    
    #4 b
    def buscar(self,newdominio):
        indice = 0
        cont = 0
        for indice in range (len(self.__listaEmails)):
            if self.__listaEmails[indice].getDominio() == newdominio:
                cont += 1
        return cont