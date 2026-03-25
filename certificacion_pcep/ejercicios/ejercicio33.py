print("Solución al ejercicio número 33")
try:
    texto : str = input("Ingrese un texto : ")
    iterador : int = 0
    vocales = ("a","e","i","o","u")
    cantidad_vocales : int = 0
    
    while iterador < len(texto):
        if texto[iterador] in vocales:
            cantidad_vocales = cantidad_vocales + 1
        iterador = iterador + 1
    print(f"El número de vocales en {texto} es : {cantidad_vocales}")

except ValueError as ve:
    print(f"Se ha encontrado un error. {ve}")