'''               Ejercicio 1
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:
a- El constructor.
b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:
idCuenta.: alumnopoo
dominio: gmail
tipoDominio: com
Resultado devuelto por retornaEmail: alumnopoo@gmail.com 
c- Método “getDominio()”, que retorna el dominio.
d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.
Implemente un programa que permita:
1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email) y luego imprima el siguiente mensaje:
Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.
2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.
3- Crear un objeto de clase Email, a partir de una dirección de correo, como por ejemplo: informatica.fcefn@gmail.com, wicc2019@unsj-cuim.edu, juanLiendro1957@yahoo.com, etc.
4- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes, solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta.  
b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado. 
c) Construya el diagrama de secuencia correspondiente.
'''

from claseEmail import Email
from ManejadorEmails import ManejadorEmails
import csv

def TestEmail(emails):
  archivo = open('ArchivoEmails.csv')
  reader = csv.reader(archivo,delimiter=",")
  band = True
  for fila in reader:
    aux = fila[0].split('@')
    if band:
      band = not band #saltea cabecera
    else:
      idCuenta = aux[0]
      aux2 = aux[1].split('.')
      dominio = aux2[0]
      tipoDominio = aux2[1]
      contraseña = fila[1]
      email = Email(idCuenta,dominio,tipoDominio,contraseña)
      emails.agregarEmail(email)
  archivo.close()

if __name__ == '__main__':
  #Inciso 4 a 
  emails = ManejadorEmails()
  TestEmail(emails)
  print("--- Lista de emails ---")
  print("idCuenta: dominio: tipoDominio:")
  emails.mostrarEmails()
  
  #Inciso 1
  nom1 = input("Ingrese nombre: ")
  id1 = input("Ingrese identificador de la cuenta: ")
  dom1 = input("Ingrese el dominio de la cuenta: ")
  tipoDom1 = input("Indique el tipo de dominio: ")
  contra1 = input("Elija una contraseña: ")
  email1 = Email(id1,dom1,tipoDom1,contra1)
  print("Estimado/a ",nom1,", te enviaremos tus mensajes a la dirección ",email1.retornaEmail())
  
  #Inciso 2
  contraVerif = input("Ingrese su contraseña actual para modificarla: ")
  if contraVerif == contra1:
    nuevaContra = input("Ingrese nueva contraseña: ")
    email1 = Email('id1','dom1',"tipoDom1",'nuevaContra')
    print("Contraseña actual: ",nuevaContra)
  else:
    print("La contraseña ingresada no coincide con la contraseña actual ")
  
  #Inciso 3
  nom = input("Nombre de la persona: ")
  idEmail = input("Identificación de cuenta: ")
  dom = input("Dominio: ")
  tipo = input("Tipo de dominio: ")
  contraseña = input("Nueva contraseña: ")
  email2 = Email(idEmail,dom,tipo,contraseña)
  print("Datos del correo guardado: ")
  print("Nombre: ",nom," Email: ",email2.retornaEmail())
  
  #Inciso 4 b 
  newDominio = input("Ingrese un dominio para buscar la cantidad de emails que coinciden con ese dominio: ")
  cantDom = emails.buscar(newDominio)
  print("La cantidad de emails que coinciden con el dominio dado es: ",cantDom)
