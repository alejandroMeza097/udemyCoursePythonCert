'''
Crea una lista con los nombres de 5 amigos y muestra el nombre del primer y último amigo utilizando índices. 
Luego, calcula cuántos caracteres tienen esos nombres y muestra los resultados por consola.
'''

nombres_amigos : str = ["goyo","axel","juan","fredkor","torbellino"]
print(f"El nombre de mi primer amigo es : {nombres_amigos[0]}. Esta palabra tiene {len(nombres_amigos[0])} caracteres.")
print(f"El nombre de mi ultimo amigo es : {nombres_amigos[-1]}. Esta palabra tiene {len(nombres_amigos[-1])} caracteres.")

