arquivo = float(input('Quantos Mb Tem o Seu Arquivo? Digite em MB: '))
internet = float(input('Qual a Velocidade da sua Internet? Digite em MBps: '))
print('Tempo Medio de Download e De: %.0f Minutos ' %((arquivo / internet) * 60))