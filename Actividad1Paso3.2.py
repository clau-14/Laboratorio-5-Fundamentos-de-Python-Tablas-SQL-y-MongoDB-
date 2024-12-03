""" Crear un diccionario simple que almacene información de contacto (nombre, 
correo) y mostrar sus claves y valores.  """
#  diccionario  de contacto
contactos = {
    "Anai":"ana1@example.com",
    "Carla": "carla@example.com",
    "Beatriz": "beatriz@example.com",
    "Daniela": "daniela@example.com",
    "Elen": "elen@example.com"
}

# Mostrar las claves y valores del diccionario
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre},\n Correo: {correo}")
