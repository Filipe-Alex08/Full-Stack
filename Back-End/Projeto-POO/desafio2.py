empresas = {1: set(), 2: set()}

for chave in empresas:

    texto = 'Digite o nome do trabalhador da empresa ' + str(chave) + ': '
    trabalhador = input(texto)

    while trabalhador != '':

        empresas[chave].add(trabalhador)
        trabalhador = input(texto)

apenas_uma_empresa = empresas[1].symmetric_difference(empresas[2])

print('Estes trabalhadores trabalham em apenas uma empresa: ', apenas_uma_empresa)