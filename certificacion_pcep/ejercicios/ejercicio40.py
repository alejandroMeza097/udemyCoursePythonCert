'''
Crea una función llamada ocurrencias que reciba una cadena de texto y un carácter como parámetros,
 y retorne la cantidad de veces que aparece el carácter en la cadena. Pide al usuario que ingrese una 
 cadena de texto y un carácter, y utiliza la función ocurrencias para calcular la cantidad de veces que 
 aparece el carácter en la cadena. Muestra el resultado por consola.

Nota: Debes usar e investigar el método "count()"

'''

def ocurrencias(texto : str, caracter : str) -> int:
    contador_caracter : int = 0
    for letra in texto:
        if letra == caracter:
            contador_caracter = contador_caracter + 1
    return contador_caracter


print(ocurrencias("karime abigail","a"))