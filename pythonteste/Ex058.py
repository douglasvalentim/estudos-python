from random import randint
from time import sleep

'''n = 0
n1 = 1
tentativas = 0

while n != n1:
    print('VOU PENSAR EM UM NÚMERO DE 1 A 10. TENTE ADVINHAR...')
    sleep(0.5)
    n = randint(0, 10)
    n1 = int(input('Em qual número eu pensei? '))
    tentativas += 1
    print('PROCESSANDO')
    sleep(0.5)
    if n1 == n:
        print('Parabéns! Eu pensei em {} e você advinhou!'.format(n))
        print('Você precisou de {} tentativas para me vencer.'.format(tentativas))
    else:
        print('Você errou, eu pensei em {}. Tente novamente!'.format(n))

print('FIM DE JOGO!')'''
n1 = int(input('Digite o número: '))
n = randint(1, 10)
tentativas = 0
while n1 != n:
    print('Eu pensei no número {}, você perdeu! Tente novamente!'.format(n))
    n = randint(1, 10)
    n1 = int(input('Tente novamente: '))
    tentativas += 1
print('Eu pensei no número {} e você também! Você ganhou'.format(n))
print('Você tentou {} para conseguir vencer.'.format(tentativas))
