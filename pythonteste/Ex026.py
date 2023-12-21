frase = str(input('Digite uma frase:')).upper().strip()
print('Sua frase tem {} letras A'.format(frase.count('A')))
print('A primeira letra A vai aparecer na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
