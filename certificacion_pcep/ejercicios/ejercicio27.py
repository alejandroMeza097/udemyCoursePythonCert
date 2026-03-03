try:
    nombre : str = input('Ingrese su nombre :')
    apellido : str = input('Ingrese su apellido : ')
    edad : int = int(input('Ingrese su edad :'))
    diccionario_usuario = {}
    diccionario_usuario["nombre"] = nombre
    diccionario_usuario["apellido"] = apellido
    diccionario_usuario["edad"] = edad
    print(f"Hola, {diccionario_usuario['nombre']} {diccionario_usuario['apellido']}. Tienes {diccionario_usuario['edad']} años.")

except ValueError as ve:
    print(f"[ERROR] : {ve}")