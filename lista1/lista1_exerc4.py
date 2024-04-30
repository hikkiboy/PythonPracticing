import math 

A = int(input("insira a: "))
B = int(input("insira b: "))
C = int(input("insira c: "))

calcR = math.pow(A + B, 2)
calcS = math.pow(B + C, 2)

calcD = (calcR + calcS) // 2

print(calcD)