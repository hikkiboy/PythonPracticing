valores = []
valor = 0
while valor >= 0 :
    valor = int(input("fala ai :"))
    valores.append(valor)
    if valor < 0 :
        break
print(sum(valores))
print(sum(valores) / len(valores))
print(len(valores))


