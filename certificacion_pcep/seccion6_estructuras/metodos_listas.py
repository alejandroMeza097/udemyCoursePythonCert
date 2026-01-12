frutas = ['coco','kiwi','uva']
frutas.append('banana')
print(frutas)
frutas.insert(0,'fresa')
print(frutas)
frutas.remove('coco')
print(frutas)
print(len(frutas))
del frutas[2]
print(frutas)

numeros = [1,7,9,3,54,789,56,90]
print(numeros)
print(sorted(numeros,reverse=True))
numeros.sort(reverse=True)
print(numeros)