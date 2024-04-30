C = input("insira o codigo: ")
N = int(input("quantas horas ?"))

sawce = 0


if(N >= 50 & N > 0):
    sawce = 50 * 10
    exc = N - 50
    E = exc * 20.0
    sawce2 = sawce + E
    print(f"salario: {sawce2}")
else:
    sawce = N * 10
    print(f"salario: {sawce}")
