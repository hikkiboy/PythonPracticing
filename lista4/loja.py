lista_prod = []
op = ""
while op != "S":
    print("da as ideia: ")
    print("Cadastrar\nExcluir\nListar")
    op = input("Digita fio: ")
    if(op == "C"):
        desc = input("Descrição: ")
        valor = float(input("Valor: "))
        produto = {
            "Descrição": desc,
            "Valor": valor,
            "Estoque": 10
        }
        lista_prod.append(produto)
    if (op == "L"):
        if len(lista_prod) == 0:
            print("Ta vazio menzinho")
        else:
            print(lista_prod)
    if(op == "E"):
        remov = int(input("Coloca o ID que vc qr tirar da lista: "))
        del lista_prod[remov]
    if(op=="S"):
        break
print("que se foda")    