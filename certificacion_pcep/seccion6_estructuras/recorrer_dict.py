miDiccionario = {"nombre":"Alejandro","edad":29,"idioma":"ingles"}
for key in miDiccionario.keys():
    print(key)

for value in miDiccionario.values():
    print(value)

for key,value in miDiccionario.items():
    print(f"key : {key} | value : {value}")
