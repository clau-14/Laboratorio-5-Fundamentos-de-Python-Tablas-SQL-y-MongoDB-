#Paso 2. Condicionales y Bucles 

"""Crear un script que pida al usuario un número y determine si es par o impar 
utilizando condicionales (if, else).
""" 

# Solicite al usuario que ingresar un número
numero = int(input("Ingresa un número: "))

#  condicionales para determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


