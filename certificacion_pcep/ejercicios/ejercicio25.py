print("Solucion al ejercicio 25")
try:
    numeros : str = input("Ingrese una secuencia de numeros separados por comas : ")
    tupla_numeros_str : tuple[str] = tuple(numeros.split(','))
    lista_numeros_int : list[int] = [int(numero_str) for numero_str in tupla_numeros_str]
    suma_numeros : int = sum(lista_numeros_int)
    producto_numeros : int = 1
    for numero in lista_numeros_int:
        producto_numeros = producto_numeros * numero
    
    print(f"La suma de los numeros es : {suma_numeros}")
    print(f"El producto de los numeros es : {producto_numeros}")
except ValueError:
    print("Has ingresado un valor incorrecto")