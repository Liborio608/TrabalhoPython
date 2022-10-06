id = []
alt = []
for i in range(1, 6):
    print('Pessoa %d' %i)
    idade = int(input('Sua Idade: '))
    altura = float(input('Sua Altura: '))
    id.append(idade)
    alt.append(altura)

print('Ordem inversa')
print('Total de Alturas')
print(alt[::-1])
print('Total de Idades')
print(id [::-1])

print('Ordem Original')
print('Total de Alturas:')
print(alt)

print('Total de Idades:')
print(id)