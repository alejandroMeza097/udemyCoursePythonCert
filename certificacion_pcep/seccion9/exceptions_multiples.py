try:
    primer_numero : int = int(input("Ingrese el primer numero : "))
    segundo_numero : int = int(input("Ingrese el segundo numero : "))
    resultado : int = primer_numero / segundo_numero
    print(resultado)

except ValueError as verr:
    print(f"[ERROR] : {verr}")
    
except ZeroDivisionError as zderr:
    print(f"[ERROR] : {zderr}")

