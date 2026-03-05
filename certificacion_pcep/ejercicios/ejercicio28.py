print("Solucion al ejercicio 27. Diccionarios")
try:
    numeros : str = input("Ingrese 3 numeros separados por coma : ")
    numeros_list_str : list[str] = numeros.split(",",) 

    #validacion para cantidad de numeros ingresados...
    if len(numeros_list_str) > 3:
        raise ValueError("Error en la cantidad de numeros ingresados")
    

    numeros_lista_int : list[int] = [int(numero_str) for numero_str in numeros_list_str]
    suma : int = sum(numeros_lista_int)
    producto : int = 1
    for numero in numeros_lista_int:
        producto = producto * numero
    diccionario_operaciones = {"suma":suma,"producto":producto}
    print(f"El resultado de la suma es : {diccionario_operaciones["suma"]}\nEl resultado de la multiplicacion es :{producto}")


except ValueError as ve:
    print(f"Se presentó un error al ejecutar el programa : {ve}")