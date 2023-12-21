from time import sleep
print('-=' * 10, 'CONTAGEM PARA VIRADA', '-=' * 10)
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
sleep(0.5)
print('FELIZ ANO NOVO!')
