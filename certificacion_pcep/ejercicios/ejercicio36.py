'''
Solicita al usuario que ingrese una palabra. 
Utiliza un bucle for para mostrar por consola la palabra invertida.
'''
palabra : str = input("Ingrese una palabra : ")
palabra_invertida : str = ""
for i in range(len(palabra) - 1,-1,-1):
    palabra_invertida = palabra_invertida + palabra[i]
else:
    print(palabra_invertida)