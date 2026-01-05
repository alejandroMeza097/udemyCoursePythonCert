#Enunciado: Solicite al usuario que ingrese su nombre, edad y estatura. Imprima la información ingresada en un solo mensaje.
nombre_ususario : str = input("Ingrese su nombre por favor :")
edad_usuario : str = input("Ingrese su edad por favor : ")
estatura_usuario : float = float(input("Ingrese su estatura por favor en metros : "))

print(f"Los datos ingresados son : NOMBRE : {nombre_ususario}. EDAD : {edad_usuario}. ESTATURA : {estatura_usuario}")