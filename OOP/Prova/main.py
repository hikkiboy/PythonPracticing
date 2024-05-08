import Contas as cs
sair = False

def MainMenu():
    while sair == False:
        print("Escolha o tipo de conta: ")
        print("1 - CONTA POUPANÇA\n2 - CONTA CORRENTE\n3 - CONTA ESPECIAL\n4 - CONTA EMPRESA\n5 - CONTA ESTUDANTIL\n6 - SAIR")
        op = int(input("Digite o codigo da opção: "))
        SecondMenu(op)

def SecondMenu(op):
    global sair
    if(op == 1):
        dianiver = input("Qual o seu aniversario ?: ")
        conta = cs.Poupanca(dianiver,1,10,0,True)
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo} Dia aniversario : {conta.diaAniversario}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                i = i - 1 
            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                i = i - 1
        dia = input("Que dia é hoje ?: ")
        if dia == dianiver:
            conta.Correcao(dia)
        else:
            print('nah')
        sair = True
        
    elif(op == 2):
        conta = cs.Corrente(1,1,0,True,3)
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo} Talões : {conta.NTalao}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                i = i - 1 
            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                i = i - 1
            else:
                break
        dia = input("Você quer pegar um talão?: ")
        if dia == "S":
            conta.Talao()
        else:
            print('nah')
        sair = True
    elif(op == 3):
        conta = cs.Especial(1000,1,1,0,True)
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo} Limite : {conta.Limite}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                i = i - 1 
            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                i = i - 1
            else:
                sair = True
                break
    elif( op == 4):
        conta = cs.Empresa(1,1,0,True,10000)
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo}, Emprestimo {conta.LimEmpresitmo}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                i = i - 1 
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)

            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                if conta.Saldo < 0 :
                    conta.Emprestimo(D)
                i = i - 1
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
            else:
                sair = True
                break
    elif(op == 5):
        conta = cs.Estudantil(1,1,0,True,5000)
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo}, Limite {conta.Limiteimite}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                i = i - 1 
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                i = i - 1
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
            else:
                sair = True
                break
    elif(op == 6):
        print("ta bom xau")
        
        sair = True
        
if sair == True:
    print("gOOD BYE")
else:
    MainMenu()