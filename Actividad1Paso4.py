""" -
Desarrollar un programa que simule una calculadora básica, 
permitiendo al usuario realizar sumas, restas, multiplicaciones y divisiones. """

a = int(input("Ingrese un numero"))
b = int(input("Ingrese un segundo numero"))


def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b


while  True:
    operacion = input("Señale con un simbolo la operacion que desea realizr +, - , *, / .")
    if operacion == "+":
        print(f"Resultado de la suma: {sumar(a, b)}")

    elif operacion == "-":
        print(f"Resultado de la resta: {restar(a, b)}")

    elif operacion == "*":
        print(f"Resultado de la multiplicacion: {multiplicar(a, b)}")

    elif operacion == "/":
         if b != 0:
            print(f"Resultado de la divicion: {dividir(a, b)}")
         else: print("Error: División por cero no es permitida.") 

    else: print("Opción no válida, por favor intente de nuevo.")
    break
    
    







