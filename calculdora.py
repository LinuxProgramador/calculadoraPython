#Calculadora simple


#importamos un modulo dentro de un paquete y le asipnamos un sobrenombre, ademas de dos funciones de dos modulos de la biblioteca local de python 
import matematicas.valores as ma
from os import system
from time import sleep


#limpiamos la consola y declaramos variables con el valor de retorno de la funcion valores_cal()
system("cls")
n1,n2,n3=ma.valores_cal()


#declaramos una funcion 
def operaciones(n1,n2,n3):
  

#aqui creamos la documentacion
  '''
   aqui trabajamos con los valores ingresados por el usuario en el modulo importado llamado valores, y con base a ello se le devolvera una salida de una operacion matematica 
   ademas de trabajar con una exepcion llamada ZeroDivisionError 
  '''


#aqui manejamos las excepciones, try ejecuta el codigo y except trabaja la excepcion si es que se genera
  try:


#la funcion sleep() da un tiempo de espera y system() permite ejecutar programas del sistema por medio de su comando
    sleep(1)
    system("cls")
    
    if n3 == "sumar":
#devuelve una suma
        print(n1+n2)

    elif n3 == "restar":
#devuelve una resta
        print(n1-n2)


    elif n3 == "multiplicar":
#devuelve una multiplicacion
        print(n1*n2)

    elif n3 == "dividir":
#devuelve una division con dos decimales
        print(f"{n1/n2:.2f}")

    else: 
#si el valor de la variable n3 no es "sumar, restar, multiplicar o dividir" se ejecutara esta parte de codigo que volvera a llamar a la funcion valores_cal() dentro del modulo valores en el paquete matematicas y tambien a la funcion operaciones()
         print(f"argumento de entrada invalido {n3}")
         sleep(3)
         system("cls")
         n1,n2,n3=ma.valores_cal()
         operaciones(n1,n2,n3)

#excepcion que se ejecuta si se trata de dividir dos ceros o valores nulos        
  except ZeroDivisionError:
         print(f"no se puede dividir ceros: n1 -> {n1} n2 -> {n2}")
         sleep(3)
         system("cls")
         n1,n2,n3=ma.valores_cal()
         operaciones(n1,n2,n3)
 

#llamamos a la funcion
operaciones(n1,n2,n3)


#metadatos
__name__="calculadora"
__version__="0.1"
  
