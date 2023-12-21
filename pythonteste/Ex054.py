from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - ano
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menor de idade'.format(totmenor))
