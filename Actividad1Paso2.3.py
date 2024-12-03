""" Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que 
se cumpla una condición específica.  """

#solicite la entrada del usuario hasta que se cumpla una condición específica
numero = int(input("Ingresa un número positivo: "))

# Bucle while que se ejecuta mientras el número sea negativo o cero
while numero >= 0:
   
    numero = int(input("Ingresa un número positivo: "))

# Mensaje final cuando el usuario ingresa un número positivo
print(f"¡Gracias!  el número que ingresaste no es positivo: {numero}")
