'''
Solicita al usuario que ingrese cinco números enteros separados por espacios. 
Crea una lista con los números ingresados y calcula el promedio de los números en la lista.
'''
contador : int = 0
lista_numeros : int = []
while contador <= 4:
    numero_actual : int = int(input("Ingrese un numero entero : "))
    lista_numeros.append(numero_actual)
    contador = contador + 1



print(f"El promedio de los numeros ingresados es : {sum(lista_numeros) / len(lista_numeros):.2f}")
