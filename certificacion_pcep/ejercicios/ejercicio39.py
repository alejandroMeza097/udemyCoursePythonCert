def es_primo(numero_input : int) -> bool:

    numero_divisibilidad  : int = 0

    if numero_input <= 1:
        return False

    for numero in range(1,numero_input + 1):
        if numero_input % numero == 0:
            numero_divisibilidad = numero_divisibilidad + 1
        
        if numero_divisibilidad > 2:
            break
    
    if numero_divisibilidad > 2:
        return False
    else:
        return True



for num in range(1,10000):
    print(f"{num} es primo ? {es_primo(num)}")