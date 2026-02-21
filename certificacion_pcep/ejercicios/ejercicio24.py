
try:
    nombre : str = input("Ingrese su nombre: ")
    edad : int = int(input("Ingrese su edad : "))
    informacion_usuario = (nombre,edad)
    print(f"Hola, {informacion_usuario[0]}. Tienes {informacion_usuario[1]} años.")

except ValueError as ve:
    print(f"Error al ingresar datos : {ve}")
