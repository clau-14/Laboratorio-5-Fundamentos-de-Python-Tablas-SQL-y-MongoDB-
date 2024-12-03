#paso 1
#Escribir un programa que imprima un mensaje en la consola. 
print("Hola como estas, vamos a realizar operaciones matematicas")

#Declarar variables de diferentes tipos (int, float, str) y realizar operaciones matemáticas simples.
#Concatenar cadenas de texto y utilizar funciones básicas como print() y input()
mensaje = ("Calcularemos el IMC")
print(mensaje)
edad = int(input("ingrese tu edad "))
peso = float(input("ingresa tu peso en kilogramos ")) 
altura = float(input("ingresa tu altura")) 

def operacion(peso,altura):
    resultado = peso / (altura * altura)
    return resultado

imc = operacion(peso, altura) 
print(f"Usted tiene {edad},Según su peso de {peso} Kg y su altura de {altura} m, su índice de masa corporal es {imc:.2f}")

