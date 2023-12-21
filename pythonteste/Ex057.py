sexo = str(input('Digite o seu sexo: ')).strip().upper()
while sexo not in 'MF':
   sexo = str(input('Dados inválidos. Por favor, digite novamente: ')).strip().upper()
print('Sexo {} cadastrado com sucesso!'.format(sexo))
