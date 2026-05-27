def saludo(nombre : str, calidez : str = "buen") -> str:
    return f"Le doy un {calidez} saludo. Mi estimado/Estimada : {nombre}"


print(saludo("alejandro"))
print(saludo("kari","excelente"))