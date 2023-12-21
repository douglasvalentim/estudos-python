import random
import time
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADVINHAR...')
n = int(random.randint(0, 5))
n1 = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
time.sleep(3)
if n1 == n:
    print('Você venceu!')
else:
    print('Eu pensei no número {}. Você perdeu!'.format(n))
print('### FIM DE JOGO ###')
