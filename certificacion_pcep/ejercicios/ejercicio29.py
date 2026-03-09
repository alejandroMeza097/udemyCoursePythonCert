'''
Pide al usuario que ingrese un número entero. Utiliza un condicional para determinar si el número es par o impar y 
muestra el resultado por consola. Si el número es impar, también muestra su cuadrado.
'''
print("Solucion al ejercicio 29")
try:
    numero : int = int(input("Ingrese un numero entero :"))
    if(numero % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
        print(f"El cuadrado del numero impar es : {numero * numero}")

except ValueError as ve:
    print(f"[ERROR]. Ha opcurrio un error : {ve}")