try:
    nombre : str = input('Ingrese su nombre :')
    apellido : str = input('Ingrese su apellido : ')
    edad : int = int(input('Ingrese su edad :'))
    diccionario_personal = {"nombre":nombre,"apellido":apellido,"edad":edad}
    print(f"Hola, {diccionario_personal['nombre']} {diccionario_personal['apellido']}. Tienes {diccionario_personal['edad']} años.")

except ValueError as ve:
    print(f"[ERROR] : {ve}")