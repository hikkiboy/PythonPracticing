pesoTomate = int(input("Qual o pesinho do mano: "))

if(pesoTomate >= 50):
    Exc = pesoTomate - 50
    Multa = Exc * 4
    print(f"Voce vai pagar {Multa} de multa")
else:
    print("Não vais pagar multa")