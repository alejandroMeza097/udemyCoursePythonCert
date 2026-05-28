from math import pi

def calcularArea(radio : float)-> float :
    return pi*pow(radio,2)

radio : float = 3
area : float = calcularArea(radio)

print(f"El area de un circulo de radio {radio} es : {area:.2f}")