def leitura():
    quantidade = int(input('Digite a quantidade de valores: '))
    lista = []
    for _ in range(quantidade):
        num = float(input('Digite um valor: '))
        lista.append(num)
    return lista

def soma(args):
    total = 0
    for num in args:
        total += num
    return total

def media(args):
    return soma(args) / len(args)

def subtrai(lista, valor):
    nova_lista = []
    for num in lista:
        nova_lista.append(num - valor)
    return nova_lista

def quadrado(lista):
    nova_lista = []
    for num in lista:
        nova_lista.append(num**2)
    return nova_lista

def raiz(valor):
    return valor**0.5

def desvio_padrao(lista):
    return raiz(media(quadrado(subtrai(lista, media(lista)))))

def main():
    lista = leitura()
    resultado = desvio_padrao(lista)
    print('O desvio padrão dessa população é: ' + str(resultado))

if __name__ == '__main__':
    main()

