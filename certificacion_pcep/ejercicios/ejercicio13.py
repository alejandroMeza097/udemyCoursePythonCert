#Ejercicio intermedio

#Crea tres variables con números enteros y calcula lo siguiente:
#El producto de los tres números.
#La suma del primero y el segundo número, dividida por el tercer número.
#El promedio de los tres números.
#Muestra los resultados por consola utilizando f-strings.

numero_entero_1 : int = 100
numero_entero_2 : int = 200
numero_entero_3 : int = 300

producto_enteros : int = numero_entero_1 * numero_entero_2 * numero_entero_3
suma_division_enteros : int = (numero_entero_1 + numero_entero_2) / numero_entero_3
promedio_enteros : float = (numero_entero_1 + numero_entero_2 + numero_entero_3) / 3

print(f"El prodcuto de los tres números enteros es : {producto_enteros}")
print(f"La suma de los primeros dos enteros y la división entre el tercer número entero es : {suma_division_enteros:.2f}")
print(f"El promedi ode los 3 números enteros es  : {promedio_enteros:.2f}")