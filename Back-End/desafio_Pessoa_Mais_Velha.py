pessoas = {
    'João': 23,
    'Maria': 28,
    'Pedro': 35,
    'Lucas': 19
}

idade_joao = pessoas['João']
pessoas['Ana'] = 31

def maior_idade(dic):
    maior_idade_pessoa = ""
    idade_maior = 0
  
    for nome, idade in dic.items():
        if idade > idade_maior:
            idade_maior = idade
            maior_idade_pessoa = nome
 
    return maior_idade_pessoa

mais_velha_pessoa = maior_idade(pessoas)
print("A pessoa mais velha é:", mais_velha_pessoa)