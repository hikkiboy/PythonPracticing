import math

pontoX1 = int(input("ponto X1: "))
pontoY1 = int(input("ponto Y1: "))
pontoX2 = int(input("ponto X2: "))
pontoY2 = int(input("ponto Y2: "))

calcDistancia = math.sqrt((math.pow(pontoX2 - pontoX1, 2)) + (math.pow(pontoY2 - pontoY1, 2)))

print(calcDistancia)