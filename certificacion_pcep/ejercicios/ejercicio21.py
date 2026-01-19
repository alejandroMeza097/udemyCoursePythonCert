'''
Solicita al usuario que ingrese cinco números enteros separados por espacios. 
Crea una lista con los números ingresados y calcula el promedio de los números en la lista.
'''

numeros : str = input("Ingresa los numeros enteros separados por espacios : ")
lista_numeros : int = list(map(int,numeros.split()))
print(lista_numeros)
print(type(lista_numeros))