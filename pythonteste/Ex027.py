nome = str(input('Digite seu nome completo:')).strip()
resultado = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(resultado[0]))
print('Seu último nome é {}'.format(resultado[len(resultado)-1]))
