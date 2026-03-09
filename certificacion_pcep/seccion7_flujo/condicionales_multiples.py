calificacion : int = 80

# Calificacion menor  59  - insuficiente

if calificacion >= 0 and calificacion <= 59:
    print("INSUFICIENTE")
elif calificacion >= 0 and calificacion <= 70:
    print("BUENO")
elif calificacion >= 0 and calificacion <= 80:
    print("MUY BUENO")
elif calificacion >= 0 and calificacion <= 100:
    print("EXCELENTE")
else:
    print("CALIFICACION NO VALIDA")