import keyword
print(f'Numero total de palabras clave : {len(keyword.kwlist)}')
print(f'Las palabras clave son : {keyword.kwlist}')
palabra : str = 'Pass'
print(f'La palabra {palabra} es clave : {keyword.iskeyword(palabra)}')

