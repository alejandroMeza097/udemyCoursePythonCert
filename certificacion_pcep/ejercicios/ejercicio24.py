
try:
    nombre : str = input("Ingrese su nombre: ")
    edad : int = int(input("Ingrese su edad : "))
    informacion_usuario = (nombre,edad)
    print(f"Hola, {nombre}. Tienes {edad} años.")

except ValueError as ve:
    print(f"Error al ingresar datos : {ve}")
