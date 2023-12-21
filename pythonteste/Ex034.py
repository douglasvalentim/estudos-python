salario = float(input('Digite o valor do seu salário:'))
if salario > 1250.00:
    s1 = salario + (salario * 0.10)
    print('Seu novo salário será de R${:.2f}'.format(s1))
else:
    s1 = salario + (salario * 0.15)
    print('Seu novo salario será de R${:.2f}'.format(s1))
