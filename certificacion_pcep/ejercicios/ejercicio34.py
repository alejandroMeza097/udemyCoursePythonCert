'''
Solicita al usuario que ingrese un número entero. Utiliza un bucle while para calcular la suma de 
todos los números impares desde el 1 hasta el número ingresado, pero solo suma aquellos impares que 
son múltiplos de 3. Muestra por consola la suma de esos números impares.
'''

print("Solucion al ejercicio 34")
try:
    numero_ingresado : int = int(input("Ingresa un numero entero : "))
    if numero_ingresado < 0:
        raise ValueError("No son admitidos enteros negativos")
    
    numeros_impares : list[int] = []
    numero_actual : int = 1

    while numero_actual <= numero_ingresado:
        if numero_actual % 3 == 0 and numero_actual % 2 != 0:
            numeros_impares.append(numero_actual)
        numero_actual += 1

    print(f"La suma de : {numeros_impares} es : {sum(numeros_impares)}")

except ValueError as ve:
    print(f"[ERROR]- Se ha encontrado un error. {ve}")