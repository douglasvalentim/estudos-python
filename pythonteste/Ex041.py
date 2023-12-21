from datetime import date

birth = int(input('Digite o ano de nascimento:'))
atual = date.today().year
idade = atual - birth
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: Mirim')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: Infantil')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: Junior')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: Sênior')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: Master')
