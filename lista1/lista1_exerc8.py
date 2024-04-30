valorCarro = float(input("Digite o valor do carro: "))

calcValorDist = (valorCarro * 0.28)
calcValorImpost = (valorCarro * 0.45)

calcValorConsum = calcValorDist + calcValorImpost

print(calcValorConsum + valorCarro)