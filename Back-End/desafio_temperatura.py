def imprimir_temperatura(valor, unidade='C', com_texto=False):
    if com_texto:
        print('A temperatura é: ', end='')

    print(valor, end='')

    if unidade == 'C':
        print('°C')
    elif unidade == 'F':
        print('°F')
    elif unidade == 'K':
        print('K')
        
def maior_numero(*numeros):
    if len(numeros) == 0:
        return None
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero      
    return maior

def imprimir_produto(nome, **dados):
    descricao = "Produto: " + nome + '\n'
    for chave, valor in dados.items():
        descricao += f"{chave}:  {valor}\n"
    print(descricao)
    
def soma(a, b):
    c = a + b
    return c

celsius_para_fahrenheit = lambda celsius: (celsius * 9/5) + 32
soma2 = lambda a,b: a+b

def main():
    print(soma2(6,9))
    
    
if __name__ == '__main__':
    main()