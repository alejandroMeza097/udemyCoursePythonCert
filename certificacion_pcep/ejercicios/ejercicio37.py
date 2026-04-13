'''
Pide al usuario que ingrese un número entero. Utiliza un bucle for para calcular la suma de todos los números 
impares desde el 1 hasta el número ingresado, pero solo suma aquellos impares que son múltiplos de 3.
Muestra por consola la suma de esos números impares.
'''

try:
    lista_multiplos_tres : list[int] = []
    numero_entero : int = int(input("Ingresa un numero entero :"))
    for numero in range(1,numero_entero + 1,1):
        if numero % 3 == 0 and numero % 2 != 0:
            lista_multiplos_tres.append(numero)

    print(f"La lista de numero es : {lista_multiplos_tres}")
    print(f"La suma de esta lista es : {sum(lista_multiplos_tres)}")

except ValueError as ve:
    print(f"[ERROR] {ve}")