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
    label_.grid(row=0, column=0)
    for codigo in codigos[1:]:
        comando = lambda b=codigo,v=vars: botao_pressionado(b,v)
        botao = tk.Button(frame_botoes, image=imagens[codigo], 
            width=54, height=54, cursor='hand2', command=comando,
            bg='#999', borderwidth=0, activebackground='#999')
        botao['relief'] = 'flat'
        botao.grid(row=l, column=c)
        botoes[codigo] = botao
        c += 1
        if c > 3:
            c = 0
            l += 1
    return botoes

def botao_pressionado(botao, vars):
    MUL = '×'
    DIV = '÷'
    
    if vars['operacao'].get() == '':

        label = 'resultado'

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

        if botao == '+':
            vars['operacao'].set('+')
            vars['operando'].set('0')

        if botao == '-':
            vars['operacao'].set('-')
            vars['operando'].set('0')

        if botao == 'mul':
            vars['operacao'].set(MUL)
            vars['operando'].set('0')

        if botao == 'div':
            vars['operacao'].set(DIV)
            vars['operando'].set('0')

    else:

        label = 'operando'
        
        if botao == 'ce':
            vars['operacao'].set('')
            vars['operando'].set('')

        if botao == '=':
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

        elif botao == '-' and not '-' in vars['operando'].get():
            vars['operando'].set('-' + vars['operando'].get())


    # Checar botões que escrevem números
    if botao in ('0','1','2','3','4','5','6','7','8','9'):
        if vars[label].get() == '0':
            vars[label].set(botao)
        elif vars[label].get() == '-0':
            vars[label].set('-' + botao)
        else:
            vars[label].set(vars[label].get() + botao)

    elif botao == 'back':
        vars[label].set(vars[label].get()[:-1])
        if vars[label].get() == '':
            vars[label].set('0')
        elif vars[label].get() == '-':
            vars[label].set('0')
        # elif vars[label].get()[-1] == '.':
        #     vars[label].set(vars[label].get()[:-1])

    elif botao == 'dot':
        if '.' not in vars[label].get():
            vars[label].set(vars[label].get() + '.')

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
    codigos = ['','ce','c','back',
            '1x','x2','rx','div',
            '7','8','9','mul',
            '4','5','6','-',
            '1','2','3','+',
            '+-','0','dot','=']

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
    frame_resultado = tk.Frame(frame_principal, bg='#999')
    frame_resultado.pack(fill='x')

    # Criar entry do =
    label_igual = tk.Label(frame_resultado, text='=',
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='w')
    label_igual.pack(side='left', fill='y')

    # Criar entry do resultado
    resultado = tk.StringVar(janela, '0')
    label_resultado = tk.Label(frame_resultado, textvariable=resultado,
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='e')
    label_resultado.pack(side='right', fill='both', expand=True)

    # Criar frame da operacao
    frame_operacao = tk.Frame(frame_principal, bg='#999')
    frame_operacao.pack(fill='x')

    # Criar entry da operacao
    operacao = tk.StringVar(janela, '')
    label_operacao = tk.Label(frame_operacao, textvariable=operacao,
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='w')
    label_operacao.pack(side='left', fill='y')

    # Criar entry do valor do operando
    operando = tk.StringVar(janela, '')
    label_operando = tk.Label(frame_operacao, textvariable=operando,
        bg='#333', fg='#fff', padx=5, pady=5, font=fonte_label,
        anchor='e')
    label_operando.pack(side='right', fill='both', expand=True)

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