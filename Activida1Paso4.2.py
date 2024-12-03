import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("He seleccionado un número entre 1 y 100. Trata de adivinarlo.")

    while not adivinado:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("El número secreto es mayor.")
            elif adivinanza > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un número válido.")


juego_adivinanza()
