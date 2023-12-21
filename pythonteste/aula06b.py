n = int(input('Digite um número:'))
print('O sucessor de {} é {} e o antecessor é {}'.format(n, n+1, n-1))

n = int(input('Digite um número:'))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, n*2, n*3, n**(1/2)))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2)/2
print('A média do aluno foi {:.1f}'.format(media))

m = int(input('Digite a distância em metros:'))
print('{} metros tem {} centímetros ou {} milímetros'.format(m, m*100, m*1000))

n = int(input('Digite um número:'))
print('A tabuada de {} é \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9))

n = float(input('Quantos reais você tem?'))
print('Você pode comprar {:.2f} dólares'.format(n*3.27))

alt = float(input('Qual a altura da parede?'))
lar = float(input('Qual a largura da parede?'))
a = alt * lar
print('A área da parede é {}m² e você vai precisar de {} litros de tinta para pintar a parede'.format(a, a/2))

p = float(input('Digite o valor do produto:'))
print('O produto tem 5% de desconto e está por R${:.2f}'.format(p*0.95))

s = float(input('Digite o seu salário:'))
print('O seu novo salário será de {:.2f} no próximo mês'.format(s*1.15))
