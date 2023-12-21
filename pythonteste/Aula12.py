nome = str(input('Qual o seu nome?'))
if nome == 'Douglas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Cristina Viviane':
    print('Que belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenho um bom dia!'.format(nome))
