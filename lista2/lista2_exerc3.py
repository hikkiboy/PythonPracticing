import math

numero1 = int(input("insira numero: "))
numero2 = int(input("insira numero: "))
numero3 = int(input("insira numero: "))
numero4 = int(input("insira numero: "))

qd1 = math.pow(numero1,2)
qd2 = math.pow(numero2,2)
qd3 = math.pow(numero3,2)
qd4 = math.pow(numero4,2)

if(qd3 >= 1000):
    print(qd3)
else:
    print(f'Numero 1 : {numero1}, Quadrado : {qd1}\nNumero 2 : {numero2}Quadrado : {qd2}\n Numero 3: {numero3}, Quadrado: {qd3}\n4: {numero4}, {qd4}')
