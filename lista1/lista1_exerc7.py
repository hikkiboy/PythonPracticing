A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))
D = int(input("Digite D: "))
E = int(input("Digite E: "))
F = int(input("Digite F: "))

calcX = ((C * E) - (B * F) / (A * E) - (B * D))
calcY = ((A * F) - (C * D) / (A * E) - (B * D))

print(f"Valor do x {calcX}\nValor do Y {calcY}")