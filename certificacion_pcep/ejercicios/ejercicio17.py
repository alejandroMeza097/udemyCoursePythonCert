'''
Solicita al usuario que ingrese dos palabras. Luego, 
concatena las palabras y muestra el resultado por consola, 
pero separa las palabras con un guion.
'''
palabra_1 : str = input("Ingrese la primer palabra por favor : ")
palabra_2 : str = input("Ingrese la segunda palabra por favor : ")
palabra_resultante : str = palabra_1 + " " +palabra_2
palabra_resultante_guion : str = palabra_resultante.replace(" ","-")
print(palabra_resultante_guion)