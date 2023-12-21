import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = (co**2 + ca**2) ** (1/2)
print('O valor da hipotenusa é {:.2f}' .format(h))


co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
