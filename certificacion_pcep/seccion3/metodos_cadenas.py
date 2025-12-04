texto : str = "Hola Mundo"
texto_2 : str = "------Hola--mundo---"
texto_3 : str = "Hola,mundo,loco"

print(texto.capitalize())
print(texto.lower())
print(texto.upper())
print(len(texto))
print(texto.replace("Mundo","Mundis"))
print(texto_2.strip("-"))
print(texto.split())
print(texto_3.split(","))
print(texto.split("o"))