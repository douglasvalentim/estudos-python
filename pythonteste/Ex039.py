from datetime import date

birth = int(input('Digite o ano que você nasceu:'))
atual = date.today().year
resultado = atual - birth
sexo = int(input('Qual seu sexo?\n[ 1 ] Homem \n[ 2 ] Mulher\n->'))
if sexo == 1:
    if resultado < 18:
        ano = birth + 18
        print('Você ainda não precisa se alistar')
        print(f'Faltam {18 - resultado} para o seu alistamento')
        print(f'Seu alistamento vai se no ano de {ano}')
    elif resultado == 18:
        print('Você precisa se alistar imediatamente!')
    else:
        ano = birth + 18
        print('Já passou do ano do seu alistamento')
        print(f'Você está {resultado - 18} anos atrasado!')
        print(f'Seu alistamento foi no ano de {ano}')
else:
    print('Você não precisa se alistar')
