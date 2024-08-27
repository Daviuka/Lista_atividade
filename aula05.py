#lista = ['dias', 30, true, 1.60]

lista1 = [1,2,3,4,5,6,7,8,8,9,10]

print(lista1[0])
print(lista1[2:])
# indices negativos sao tratados de maneira especial, o -1 é considerado o ultimo elemento
print(lista1[-1])

lista_int = [1,2,3,4,5,6,7,8,8,9,10]
print(lista_int)
lista_int.sort()

print(lista_int)
lista_int.sort(reverse=True)

print(lista_int)
print(f'Lista ordenada direto no print: {sorted(lista_int, reverse=True)}')

# remove, pop, del

nomes = ['dias, gomes, jona, arthur, kaun, gomes']
print(nomes)

nomes.remove('gomes')
print(nomes)

momes.pop(1)

print(nomes)













