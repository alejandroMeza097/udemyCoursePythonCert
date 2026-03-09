'''
Solicita al usuario que ingrese una cadena de texto. Utiliza un condicional para determinar si la cadena 
tiene una longitud mayor a 10 caracteres. Si es mayor a 10 caracteres, muestra por consola la cadena en mayúsculas. 
Si no, muestra la cadena en minúsculas.
'''
print("Solucion al ejercicio 30")
try:
    #SE RECUPERA LA INFORMACION DEL USUARIO
    texto_usuario : str = input("Ingrese una cadena de texto : ")

    #SE VERIFICA QUE NO SEAN SOLO ESPACIOS
    if(len(texto_usuario.strip()) == 0  or texto_usuario is None):
        raise ValueError("No se ha ingresado niungun valor")
    else:
        #SE VERIFICA QUE NO SEAN DIGITOS
        for letra in texto_usuario:
            if letra.isdigit():
                raise ValueError("Se encontró un digito en la cadena")
            
        #SE VERIFICA EL TAMAÑO DE LA CADENA
        if(len(texto_usuario) > 10):
            print(f"El texto en mayusculas : {texto_usuario.upper()}")
        else:
            print(f"El texto en minusculas : {texto_usuario.lower()}")
    
except ValueError as ve:
    print(f"[ERROR]. Ha ocurrido un error. {ve}")