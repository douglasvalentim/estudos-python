import math

a = float(input('Digite o ângulo:'))
cosseno = math.cos(math.radians(a))
seno = math.sin(math.radians(a))
tangente = math.tan(math.radians(a))
print('O seno de {:.1f}º é {:.2f}'.format(a, seno))
print('O cosseno de {} é {:.2f}'.format(a, cosseno))
print('A tangente de {} é {:.2f}'.format(a, tangente))
