saldo : float = 500
retiro : float = 501
if saldo > retiro:
    print("Retiro permitido")
    saldo = saldo - retiro
    print(f"Saldo actual {saldo}")
else:
    if saldo >= (retiro - 100):
        print("Retiro permitido con sobregiro")
    else:
        print("Retiro no permitido")