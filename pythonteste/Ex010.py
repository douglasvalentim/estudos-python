d = float(input('Quantos km você percorreu?'))
t = float(input('Quantos dias você ficou com o carro?'))
p = ((d * 0.15) + (t * 60))
print('O valor total do aluguel do seu carro é de R${:.2f}.'.format(p))
