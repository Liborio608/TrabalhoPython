kg = float(input("Quantos Kg você Pescou: " ))
limite = 0
multa = 0
if kg <= 50:
    print("Parabéns você nao Ultrapassou o limite! ")
else:
    limite = kg - 50
    multa = limite * 4
    print("Você ultrapassou o limite de: %.2f" "Kg" %limite)
    print("Sua multa e no valor de: %.2f" "R$" %multa)