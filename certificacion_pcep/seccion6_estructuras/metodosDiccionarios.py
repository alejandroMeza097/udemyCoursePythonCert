persona = {"nombre":"alex meza","ciudad":"puerto escondido","edad":29}

#imprimiendo solamente las claves
for key in persona.keys():
    print(key)

#imprimiendo solo valores
print(persona.values())


#uso de metodo get. Sirve para obtener los valores de una clave
print(persona.get("nombre","Valor no encontrado"))

print(len(persona))
