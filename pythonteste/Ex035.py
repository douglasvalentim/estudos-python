print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
l1 = float(input('Digite o comprimento do primeiro lado:'))
l2 = float(input('Digite o comprimento do segundo lado:'))
l3 = float(input('Digite o comprimento do terceiro lado:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem gerar um triangulo.')
else:
    print('Os segmentos acima não podem formar um triangulo.')
