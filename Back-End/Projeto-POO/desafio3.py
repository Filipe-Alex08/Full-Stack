raizes = {}

texto = 'Digite um número inteiro: '
numero = input(texto)

while numero != '':

    numero = int(numero)

    if numero in raizes:
        print('Achou no dicionário: ', raizes[numero])
    else:
        raizes[numero] = numero**0.5
        print('Calculou: ', raizes[numero])
    
    numero = input(texto)