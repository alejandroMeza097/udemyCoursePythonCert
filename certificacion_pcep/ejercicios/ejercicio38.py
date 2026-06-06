def saludar(nombre : str) -> str:
    return f"Hola {nombre}. Espero estes bien."

nombre_input : str = input("Ingresa tu nombre : ")
print(f"Saludo personalizado : {saludar(nombre_input)}")