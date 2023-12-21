n1 = 0
n2 = 0
r = 0

while r != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA
    --> Escolha uma opção:''')
    r = int(input(''))
    if r == 1:
        print('A soma dos números digitados é {}'.format(n1 + n2))
    elif r == 2:
        print('O produto dos números digitados é {}'.format(n1 * n2))
    elif r == 3:
        print('O maior número entre {} e {} é {}.'.format(n1, n2, max(n1, n2)))
print('FIM')

