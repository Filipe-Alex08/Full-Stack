alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

frase = input('Digite a frase: ')

usadas = set(frase)

usadas.discard(' ')

nao_usadas = alfabeto - usadas

print('Usou: ', usadas)
print('Não usou: ', nao_usadas)
