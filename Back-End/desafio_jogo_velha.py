import tkinter as tk
from tkinter import messagebox

def criar_botoes():

    botoes = []

    for linha in range(3):

        botoes_linha = []
        for coluna in range(3):

            comando = lambda l=linha, c=coluna: fazer_jogada(l, c)
            botao = tk.Button(frame_botoes, image=imagens['invisivel'], 
                width=100, height=100, cursor='hand2', command=comando)
            botao.grid(row=linha, column=coluna)
            botoes_linha.append(botao)

        botoes.append(botoes_linha)

    return botoes

def fazer_jogada(linha, coluna):

    if tabuleiro[linha][coluna] is None:

        tabuleiro[linha][coluna] = jogadas['atual']
        buttons[linha][coluna].config(image=imagens[jogadas['atual']], 
            width=100, height=100,cursor='arrow')
        buttons[linha][coluna]['relief'] = 'sunken'

        if checar_vencedor():
            messagebox.showinfo('Vitória', f"Jogador {jogadas['atual']} venceu!")
            reiniciar_jogo()
        elif jogadas['restantes'] == 1:
            messagebox.showinfo('Empate', 'O jogo empatou')
            reiniciar_jogo()
        else:
            jogadas['atual'] = 'O' if jogadas['atual'] == 'X' else 'X'
            jogadas['restantes'] -= 1

def checar_vencedor():

    # Checar linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == jogadas['atual']:
            return True

    # Checar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogadas['atual']:
            return True

    # Checar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogadas['atual']:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogadas['atual']:
        return True

    return False

# Function to reset the game
def reiniciar_jogo():

    jogadas['atual'] = 'X'
    jogadas['restantes'] = 9

    for linha in range(3):
        for coluna in range(3):
            tabuleiro[linha][coluna] = None
            buttons[linha][coluna].config(image=imagens['invisivel'])
            buttons[linha][coluna]['relief'] = 'raised'

# Initialize the game
tabuleiro = [[None, None, None],
             [None, None, None],
             [None, None, None]]

# Variáveis
jogadas = {
    'atual': 'X',
    'restantes': 9
}

# Criar a janela
janela = tk.Tk()
janela.title('Jogo da Velha')
janela.resizable(False, False)

# Carregar imagens
imagens = {
    'X': tk.PhotoImage(file='x.png'), 
    'O': tk.PhotoImage(file='o.png'),
    'invisivel': tk.PhotoImage(width=1, height=1)
}

# Mudar ícone
janela.wm_iconphoto(True, imagens['X'])

# Criar frame dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(padx=15, pady=15)
buttons = criar_botoes()

# Loop principal do Tk
janela.mainloop()