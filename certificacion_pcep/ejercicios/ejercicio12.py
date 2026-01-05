altura : float  = float(input("Ingresa tu altura en metros por favor : "))
peso : float = float(input("Ingresa tu peso en kilogramos (Kg) por favor : "))
imc : float = peso/(altura ** 2)
print(f"El indice de masa coorporal es : {imc:.2f}")