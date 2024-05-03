
lista_numeros = []
op = "A"
while op != "S":
    print("O que tu quer fazer ?: ")
    print("Inserir(I)\nListar(L)\nApagar(A)\nSair(S)")
    op = input("Aguardando: ").upper()
    if(op == "I"):
        try:
            numero = int(input("Digite o valor: "))
            lista_numeros.append(numero)
        except:
            print("não mano isso n pode")
    if(op == "L"):
        if(len(lista_numeros) == 0):
            print("A lista esta vazia")
        else:
            print("Esses são os numeros:")
            print(lista_numeros)
    if(op == "A"):
        if(len(lista_numeros) == 0):
            print("A lista esta vazia")
        else:
            inpt = int(input("Qual o id para remover "))
            del lista_numeros[inpt]
    if(op == "S"):
        break

