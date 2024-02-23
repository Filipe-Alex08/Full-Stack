resultado = float(input("Digite um número: "))

while True:
    operacao = input("Digite '+', '-', '*', '/' ou '=' para sair: ")
    
    if operacao == '=':
        print("O resultado é:", resultado)
        break
    elif operacao == '+':
        numero = float(input("Digite um número a ser somado: "))
        resultado += numero
        print("O resultado é:", resultado)
    elif operacao == '-':
        numero = float(input("Digite um número a ser subtraído: "))
        resultado -= numero
        print("O resultado é:", resultado)
    elif operacao == '*':
        numero = float(input("Digite um número a ser multiplicado: "))
        resultado *= numero
        print("O resultado é:", resultado)
    elif operacao == '/':
        numero = float(input("Digite um número para a divisão: "))
        resultado /= numero
        print("O resultado é:", resultado)
    else:
        print("Operação inválida! Tente novamente.")