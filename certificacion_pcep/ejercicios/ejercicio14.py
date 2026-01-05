from math import pi
radio : float = float(input("Ingresa el valor del radio del circulo en centímetros : "))
area : float = pi * (radio ** 2)
print(f"El área del circulo es {area:.2f} cm2")