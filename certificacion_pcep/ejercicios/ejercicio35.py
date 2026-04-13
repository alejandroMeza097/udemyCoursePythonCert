'''
Pide al usuario que ingrese su nombre. Utiliza un bucle for para mostrar por consola 
cada letra del nombre en una línea separada.
'''

try:
    nombre : str = input("Ingrese su nombre : ")
    for letra in nombre:
        print(letra)
except ValueError as ve:
    print(f"[ERROR] {ve}")