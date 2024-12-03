# Crear una lista vacía
frutas = []

# Agregar elementos a la lista
frutas.append("manzana")
frutas.append("banana")
frutas.append("cereza")

# Mostrar la lista
print(frutas)

#Implementar un script que permita al usuario agregar elementos a una lista o 
#actualizar valores en un diccionario. 
def mostrar_menu():
    print("Menú:")
    print("1. Agregar fruta a la lista")
    print("2. Mostrar lista de frutas")
    print("3. Salir")

def agregar_a_lista(lista):
    fruta = input("Ingrese la fruta a agregar: ")
    lista.append(fruta)
    print(f"Fruta '{fruta}' agregada a la lista.")

def mostrar_lista(lista):
    print("Lista de frutas:")
    for fruta in lista:
        print(f"- {fruta}")

def main():
    lista = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_a_lista(lista)
        elif opcion == "2":
            mostrar_lista(lista)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
    
    print("Lista final:", lista)

if __name__ == "__main__":
    main()



