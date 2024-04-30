segundos = int(input("tempo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600) % 60

print(f"São {horas} horas, {minutos} minutos e {segundos} segundos")