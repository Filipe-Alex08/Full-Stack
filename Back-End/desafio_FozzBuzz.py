def fizzbuzz(num):
    if num%3 == 0 and num%5 == 0:
        return 'fizzbuzz'
    elif num%3 == 0:
        return 'fizz'
    elif num %5 == 0:
        return 'buzz'
    else:
        return str(num)

def fizzbuzz_lista(lista_nums):
    nova_lista = []
    for num in lista_nums:
        nova_lista.append(fizzbuzz(num))
    return nova_lista

lista = fizzbuzz_lista(range(1,101))

print(lista)