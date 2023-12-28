#los valores entrantes de la calculadora
from os import system
from time import sleep

def valores_cal():
    '''
      aqui le pedimos al usuario que ingrese sus valores para hacer las operaciones y que operacion quiere realizar, ademas de declara las variables como globales y trabajar la exepcion ValueError
    '''
    try:
       print("Bienvenido, a continuacion se le pedira unos datos, si en algun momento quisieras salir, preciona \"CTRL_C\" ")
       n1,n2,n3=int(input("ingresa un valor numerico >> ")),int(input("ingresa un valor numerico >> ")),input("quieres sumar,restar,dividir o multiplicar >> ")

#aqui trabajamos la excepcion KeyboardInterrupt que es una excepcion generada al precionar la combinacion de teclas CTRL_C 
    except KeyboardInterrupt:
         consulta=input("en verdad deseas salir del programa? ")
         if consulta == "si":
             exit()
         else:
             system("cls")
             n1,n2,n3=valores_cal()
    
#aqui trabajamos la excepcion ValueError que se genera al ingresar un dato diferente al especificado, por ejemplo una cadena en donde se especifico un dato entero
    except ValueError:
        print("ingresaste un dato no valido, vuelve a intentarlo")
        sleep(2)
        system("cls")
        n1,n2,n3=valores_cal()


    return n1,n2,n3


