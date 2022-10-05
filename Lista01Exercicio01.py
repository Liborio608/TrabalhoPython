sexo = int(input('Digite |1| Para Sexo Masculino ou Digite |2| Para Sexo Feminino: '))
alt = float(input('Altura:'))
peso = float(input('Peso:'))
pesoid = (72.7*alt) - 58 if sexo == 1 else (62.1*alt) - 44.7
if peso < pesoid:
	print('Abaixo do peso ideal!')
elif peso == pesoid:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, pesoid))