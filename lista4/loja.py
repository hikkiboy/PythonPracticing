lista_prod = []
op = ""
while op != "S":
    print("da as ideia: ")
    print("Cadastrar\nExcluir\nListar")
        
    try:
        op = input("Digite a inicial da opção que deseja: ").upper()
    except:
        print("Fio, não é tão difícil, digita certo.")

    if(op == "C"):
        try:
            desc = input("Descrição: ")
            valor = float(input("Valor: "))
            produto = {
                "Descrição": desc,
                "Valor": valor,
                "Estoque": 10
            }
            lista_prod.append(produto)
        except:
            print("O valor não corresponde a uma opção válida!")
    if (op == "L"):
        if len(lista_prod) == 0:
            print("Ta vazio menzinho")
        else:
            for indice, item in enumerate(lista_prod):
                print(indice,lista_prod)
    if(op == "E"):
        try:
            remov = int(input("Coloca o ID que vc qr tirar da lista: "))
            del lista_prod[remov]
        except:
            print("O ID está incorreto")
    if(op=="S"):
        break
print("que se foda")    