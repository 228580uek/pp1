lista = [1,2,3,4,5]
print(lista)
#pp. a:
lista[0] -= 1
print(lista)
#pp. b:
lista[-1] += 4
print(lista)
#pp. c:
lista[len(lista)//2] *= 2
print(lista)
#pp. d:
for index in range(len(lista)):
    lista[index] += 3
print(lista)