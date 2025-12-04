'''
Slicing de cadenas
Cadenas de texto van entre comillas o comillas simples
'''
texto : str = "Hola mundo python!"
cadena_test : str = "monty python"

cadena_slice_1 : str = cadena_test[0:5]
print(f'Monty : {cadena_slice_1}')
print(f'on : {cadena_test[1:3]}')
print(texto[0])
print(texto[-1])
print(texto[-2])
print(texto[0:3])
print(texto[2:-1])
print(texto[3:])
print(texto[:6])