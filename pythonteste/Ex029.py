v = float(input('Digite a velocidade do carro:'))
if v > 80:
    m = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade de 80Km/H e foi multado em R${:.2f}'.format(m))
    print('Para mais dúvidas ligue 0800 0000')
else:
    print('Tenha um bom dia! Dirija com segurança!')
