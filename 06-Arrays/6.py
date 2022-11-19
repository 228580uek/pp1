lista = [2,3,7,5,4]
#pp. a:
print(lista)
#pp. b:
print(len(lista))
#pp. c:
print(lista[0])
#pp. d:
print(lista[1])
#pp. e:
print(lista[-1])
#pp. f:
print(lista[-2])
#pp. g:
print(lista[0] + lista[-1])
#pp. h:
print(lista[int(len(lista)/2)])
#pp. i:
for item in lista:
    print(item,end=' ')
#pp. j:
print()
for i in range(len(lista)//2+1):
    print(lista[i], end=' ')