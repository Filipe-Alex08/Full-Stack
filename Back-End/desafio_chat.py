def filtrar_mensagem(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, '*'*len(palavra))
    return texto

texto = 'joão é bobo e feio e me deve 10 reais'

palavras_proibidas = ['bobo', 'feio', 'me']

resultado = filtrar_mensagem(texto, palavras_proibidas)

print(resultado)