'''
Pide al usuario que ingrese un número entero. Utiliza condicionales para determinar si 
el número es negativo, cero o positivo. Además, indica si es par o impar. Si el número es
 positivo y par, muestra la suma de los dos primeros números de la lista [2, 4, 6, 8, 10].
'''
print("Solucion al ejercicio 31")
lista_nuemros : list[int] = [2, 4, 6, 8, 10]
try:
    numero_usuario : int = int(input("Ingrese un numero entero por favor : "))
    if numero_usuario  > 0:
        print("El numero ingresado es mayor a cero")
        if numero_usuario % 2 == 0:
            print("El numero es par")
            print(f"La suma de los dos primeros numeros de la lista es : {lista_nuemros[0] + lista_nuemros[1]}")
        else:
            print("El numero es impar")
    elif numero_usuario == 0:
        print("El numero ingresado es cero")
    else:
        print("El numero ingresado es menor a cero")

except ValueError as ve:
    print(f"[ERROR] : {ve}")