import tkinter as tk

def carregar_imagens(codigos):
    imagens = {}
    for codigo in codigos:
        imagens[codigo] = tk.PhotoImage(file='img\\button_'+codigo+'.png')
    return imagens

def criar_botoes(frame_botoes, codigos, imagens, vars):
    botoes = {}
    l = 0
    c = 1
    label_ = tk.Label(frame_botoes, image=imagens[''], bg='#999')
    label_.grid(row=0, column=0, padx=2, pady=2)
    for codigo in codigos[1:]:
        comando = lambda b=codigo,v=vars: botao_pressionado(b,v)
        botao = tk.Button(frame_botoes, image=imagens[codigo], 
            width=54, height=54, cursor='hand2', command=comando,
            bg='#999', borderwidth=0, activebackground='#999')
        botao['relief'] = 'flat'
        botao.grid(row=l, column=c, padx=1, pady=1)
        botoes[codigo] = botao
        c += 1
        if c > 3:
            c = 0
            l += 1
    return botoes

def botao_pressionado(botao, vars):
    MUL = '×'
    DIV = '÷'

    if botao == '+-':
        if float(vars['resultado'].get()) != 0:
            vars['resultado'].set(str(float(vars['resultado'].get())*-1))

    elif botao == '1x':
        if float(vars['resultado'].get()) != 0:
            vars['resultado'].set(str(1/float(vars['resultado'].get())))

    elif botao == 'rx':
        if float(vars['resultado'].get()) > 0:
            vars['resultado'].set(str(float(vars['resultado'].get())**0.5))

    elif botao == 'x2':
        vars['resultado'].set(str(float(vars['resultado'].get())**2))

    elif botao == '+':
        vars['operacao'].set('+')

    elif botao == '-':
        vars['operacao'].set('-')

    elif botao == 'mul':
        vars['operacao'].set(MUL)

    elif botao == 'div':
        vars['operacao'].set(DIV)
        
    elif botao == 'ce':
        vars['operacao'].set('')
        vars['operando'].set('')

    elif botao == '=':
        if vars['operacao'].get() == '+':
            vars['resultado'].set(str(float(vars['resultado'].get()) + float(vars['operando'].get())))
        elif vars['operacao'].get() == '-':
            vars['resultado'].set(str(float(vars['resultado'].get()) - float(vars['operando'].get())))
        elif vars['operacao'].get() == MUL:
            vars['resultado'].set(str(float(vars['resultado'].get()) * float(vars['operando'].get())))
        elif vars['operacao'].get() == DIV:
            vars['resultado'].set(str(float(vars['resultado'].get()) / float(vars['operando'].get())))
        vars['operacao'].set('')
        vars['operando'].set('')

    elif botao == 'c':
        vars['resultado'].set('0')
        vars['operacao'].set('')
        vars['operando'].set('')

def main():

    # Criar a janela
    janela = tk.Tk()
    janela.title('Calculadora')
    janela.resizable(False, False)

    # codigos das imagens e botoes
    codigos = ['','ce','c','=',
            '1x','x2','rx','+-',
            '+','-','mul','div']

    # Carregar imagens
    imagens = carregar_imagens(codigos)

    # Mudar ícone
    janela.wm_iconphoto(True, imagens['+-'])

    # Criar frame principal
    frame_principal = tk.Frame(janela, bg='#999')
    frame_principal.pack()

    # Fonte das labels
    fonte_label = ('Arial', '24', 'bold')

    # Criar frame do resultado
    frame_resultado = tk.Frame(frame_principal, bg='#333')
    frame_resultado.pack(fill='x')

    # Criar entry do =
    label_igual = tk.Label(frame_resultado, text='=',
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='w')
    label_igual.pack(side='left', fill='y')

    # Criar entry do resultado
    resultado = tk.StringVar(janela, '0')
    entry_resultado = tk.Entry(frame_resultado, textvariable=resultado,
        bg='#333', fg='#fff', font=fonte_label, justify='right', width=12)
    entry_resultado.pack(side='right', fill='y')

    # Criar frame da operacao
    frame_operacao = tk.Frame(frame_principal, bg='#333')
    frame_operacao.pack(fill='x')

    # Criar entry da operacao
    operacao = tk.StringVar(janela, '')
    label_operacao = tk.Label(frame_operacao, textvariable=operacao,
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='w')
    label_operacao.pack(side='left', fill='y')

    # Criar entry do valor do operando
    operando = tk.StringVar(janela, '')
    entry_operando = tk.Entry(frame_operacao, textvariable=operando,
        bg='#333', fg='#fff', font=fonte_label, justify='right', width=12)
    entry_operando.pack(side='right', fill='y')

    # Dicionario contendo stringvars
    vars = {'resultado': resultado, 'operacao': operacao, 'operando': operando}

    # Criar frame dos botões
    frame_botoes = tk.Frame(frame_principal, bg='#999')
    frame_botoes.pack(side='left', padx=10, pady=10)
    botoes = criar_botoes(frame_botoes, codigos, imagens, vars)

    # Loop principal do Tk
    janela.mainloop()

if __name__ == '__main__':
    main()