from random import randint

lista = [randint(0,99) for _ in range(100)]

ordenada = False

while not ordenada:

    ordenada = True

    for i in range(1, len(lista)):

        if lista[i] < lista[i-1]:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            ordenada = False

print(lista)