termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decima = termo + (10 - 1) * razao
for c in range(termo, decima + razao, razao):
    print(c, end=' ')
