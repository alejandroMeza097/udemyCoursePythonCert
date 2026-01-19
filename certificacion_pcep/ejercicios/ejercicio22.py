'''
Pide al usuario que ingrese una cadena con palabras separadas por espacios. Crea una lista con las palabras ingresadas 
y luego crea una nueva lista con las palabras ordenadas alfabéticamente.
'''
palabras : str = input("Ingrese palabras separadas por espacios : ")
lista_palabras : str = palabras.split()
lista_palabras.sort()
print(lista_palabras)