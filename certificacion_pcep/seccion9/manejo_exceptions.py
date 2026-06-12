lista_numeros : int = [1,2,3]
diccionario_numeros :dict[str,int]  = {"a":1,"b":3}

try:
    #print(lista_numeros[4])
    print(diccionario_numeros.get("a"))
except IndexError as ierr:
    print(ierr)
