area = float(input('Digite o tamanho da área que será pintada: '))

litros = area / 6
litros_lata = 18
litros_galao = 3.6
preco_lata = 80
preco_galao = 25
latas = 0
galoes = 0

while litros > litros_lata:
    litros -= litros_lata
    latas += 1

if litros > 0:

    while litros > litros_galao:
        litros -= litros_galao
        galoes += 1

    if litros > 0:
        galoes += 1

    if galoes * preco_galao > preco_lata:
        galoes = 0
        latas += 1

custo = latas*preco_lata + galoes*preco_galao

print('Você precisa de %i latas e %i galões' % (latas, galoes))
print('O custo será: %.2fR$' % custo)