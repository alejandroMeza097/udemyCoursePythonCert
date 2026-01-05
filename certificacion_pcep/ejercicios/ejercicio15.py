from math import pi
radio : float = float(input("Ingrese el valor del radio en centimetros :"))
area : float = pi * (radio ** 2)
perimetro : float = pi * 2 * radio
print(f"El area del circulo es : {area:.2f} cm2")
print(f"El perimetro del circulo es : {perimetro:.2f} cm")
