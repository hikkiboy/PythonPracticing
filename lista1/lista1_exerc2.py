idade = int(input("quantos dias você viveu? "))
idade_anos = (idade // 365)
idade_meses = (idade % 365) // 30
idade_dias = ((idade % 365) % 30)

print(f"Você viveu {idade_anos} anos\n{idade_meses} meses\ne {idade_dias} dias" )