casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento?'))
parcela = casa / (tempo * 12)
if parcela <= (salario * 0.30):
    print('Parabéns! A sua proposta foi aceita!')
else:
    print('Infelizmente a sua proposta não foi aceita.')
