d = float(input('Digite a distância da sua viagem em km:'))
if d <= 200:
    p = d * 0.5
    print('Sua passagem custará R${:.2f}'.format(p))
else:
    p1 = d * 0.45
    print('Sua passagem custará R${:.2f}'.format(p1))
