print('{:=^40}'.format('OASIS DOS PETS'))

valor = float(input('Valor da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais cartão''')
pagamento = int(input('Escolha a forma de pagamento:'))

if pagamento == 1:
    print('Você escolheu dinheiro ou cheque.')
    print('Sua compra de R${:.2f}, ficou por R${:.2f} com 10% de desconto!'.format(valor, valor - (valor * 0.10)))
elif pagamento == 2:
    print('Você escolheu cartão de débito.')
    print('Sua compra de R${:.2f}, ficou por R${:.2f} com 5% de desconto!'.format(valor, valor - (valor * 0.05)))
elif pagamento == 3:
    print('Você escolheu crédito divido em 2x SEM JUROS!\nParcela: R${:.2f}'.format(valor / 2))
    print('Sua compra é de R${:.2f}.'.format(valor))
elif pagamento == 4:
    parcela = int(input('Deseja parcelar em quantas vezes?'))
    final = valor + (valor * 0.20)
    print('Você escolheu crédito em {}.'.format(parcela))
    print('Parcela: R${:.2f}'.format(final / parcela))
    print('Sua compra de R${:.2f}, ficou por R${:.2f}, divido em {}x com juros!'.format(valor, final, parcela))
else:
    print('Por favor, digite uma opção válida!')
