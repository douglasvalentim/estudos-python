i = int(input('Início:')) #PARTE 1
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(i, f + 1, p):
    print(c)
print('FIM')

s = 0 #PARTE 2
for c in range(0, 4):
    n = int(input('Digite um número:'))
    s += n
print('O somatório dos valores foi {}'.format(s))
print('FIM!')
