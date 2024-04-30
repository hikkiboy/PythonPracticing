idade_anos = int(input("qual sua idade em anos?"))
idade_mes = int(input("qual o mes?"))
idade_dias = int(input("qual dia do mes é hoje?"))

total_dias = (idade_anos * 365) + (idade_mes * 30) + (idade_dias)
print(f"você viveu {total_dias} dias")


