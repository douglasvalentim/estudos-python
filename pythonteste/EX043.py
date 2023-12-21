a = float(input('Qual sua altura? (m)'))
p = float(input('Qual seu peso? (kg)'))
imc = p / (a ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepreso')
elif imc <= 40:
    print('Você está obeso')
else:
    print('Você está com obesidade morbida')
