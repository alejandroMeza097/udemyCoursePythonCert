print("Solucion al ejercicio número 31")
try:
    numero_ingresado : int = int(input("Ingrese un número entero : "))
    numero_actual : int = 0
    while numero_actual < numero_ingresado:
        if numero_actual % 2 == 0 and numero_actual != 0:
            print(numero_actual)
        numero_actual = numero_actual + 1

except ValueError as ve:
    print(f"[ERROR] - Ha ocurrido un error. {ve}")