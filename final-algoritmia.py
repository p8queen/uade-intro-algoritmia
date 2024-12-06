import random

def pertenece(lista, valor):
	encontrado = False
	i=0
	while not encontrado and i<len(lista):
		if lista[i] == valor:
			encontrado  = True
		i += 1
	return encontrado

def ordenar(lista):
	desordenada = True
	while desordenada:
		desordenada = False
		for i in range(len(lista)-1):
			if lista[i+1]<lista[i]:
				aux = lista[i+1]
				lista[i+1] = lista[i]
				lista[i] = aux
				desordenada = True


def insercion(lista):
	for i in range(1,len(lista)):
		aux = lista[i]
		j = i
		while j>=0 and aux<lista[j-1]:
			lista[j] = lista[j-1]
			j = j - 1
		lista[j] = aux

def busqSeuencial(lista, dato):
	i = 0
	while i<len(lista) and lista[i] != dato:
		i = i + 1
	if i<len(lista):
		return i
	else:
		return -1

def busqueda(lista, valor):
	izq = 0
	der = len(lista) - 1
	pos = -1
	while pos == -1 and izq <= der:
		centro = (izq + der) // 2
		if lista[centro] == valor:
			pos = centro
		elif valor > lista[centro]:
			izq = centro + 1
		else:
			der = centro - 1
	return pos


lista = [2,8,5,9,7]
print(lista)
print(pertenece(lista, 5))
print(pertenece(lista, 0))
#ordenar(lista)
insercion(lista)
print(lista)
print('busqueda binaria: ')
print(busqueda(lista, 8))
print(busqueda(lista, 12))
print()
print(busqSeuencial(lista, 8))
print(busqSeuencial(lista, 12))


