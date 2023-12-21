print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
l1 = float(input('Digite o primeiro segmento:'))
l2 = float(input('Digite o segundo segmento:'))
l3 = float(input('Digite o terceiro segmento:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem gerar um triangulo.')
    if l1 == l2 == l3:
        print('O triangulo é Equilátero')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triangulo é Escaleno')
    else:
        print('O triangulo é Isóceles')
else:
    print('Os segmentos acima não podem formar um triangulo.')
