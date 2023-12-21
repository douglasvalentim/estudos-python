from random import randint
from time import sleep

print('{:=^80}'.format('\033[1;40mJOKENPO\033[m'))
itens = ('pedra', 'papel', 'tesoura')
computador = (randint(0, 2))

print('''Suas opções!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
sleep(1)
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('EMPATE!')
    else:
        print('Você ganhou!')

elif computador == 2:#COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    else:
        print('EMPATE!')
