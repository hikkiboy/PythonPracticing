import Contas as cs
import pymysql
import random


conexao = pymysql.connect(
    host='localhost',
    user="root",
    password="fbradesco",
    database='banco'
)
cursor = conexao.cursor()


P1 = cs.Poupanca(None,None,None,None,None)
C1 = cs.Corrente(None,None,None,None,None)
E1 = cs.Especial(None,None,None,None,None)
EM1 = cs.Empresa(None,None,None,None,None)
ES1 = cs.Estudantil(None,None,None,None,None)

sair = False

def MainMenu():


    while sair == False:
        print("Escolha o tipo de conta: ")
        print("1 - CONTA POUPANÇA\n2 - CONTA CORRENTE\n3 - CONTA ESPECIAL\n4 - CONTA EMPRESA\n5 - CONTA ESTUDANTIL\n6 - SAIR")
        op = int(input("Digite o codigo da opção: "))
        SecondMenu(op)



def SecondMenu(op):
    global sair
    global P1

    wah = True


    if(op == 1):

            while wah:
                if P1.Numero != None: 
                    conta = P1
                    for i in range(10):
                        print(f"Saldo atual:{conta.Saldo} Dia aniversario : {conta.diaAniversario}, Numero da conta: {conta.Numero}")
                        print("Movimentos: C para Credito D para Debito")
                        
                        wa = input("Digite: ")
                        
                        
                        if(wa == "C"):
                            C = int(input("digite o valor: "))
                            conta.Credito(C)
                            salso = (conta.Saldo, conta.Numero)
                            cursor.execute("UPDATE poupanca SET saldo = %s where numero = %s",salso )
                            conexao.commit()
                            i = i - 1 


                        elif(wa == "D"):
                            D = int(input("Digite o valor: "))
                            conta.Debito(D)
                            salso = (conta.Saldo, conta.Numero)
                            cursor.execute("UPDATE poupanca SET saldo = %s where numero = %s",salso )

                            conexao.commit()
                            i = i - 1

                    dia = input("Que dia é hoje ?: ")
                    if dia == conta.diaAniversario:
                        conta.Correcao(dia)
                    else:
                        print('nah')
                else:
                    opof = input("não encontrei sua conta,  Quer tentar criar uma nova ? (C) ou tentar logar ? (L): ")
                    if opof == "C":  
                        dianiver = int(input("Qual o seu aniversario ?: "))
                        nConta = random.randint(1,99999)
                        cpf = input("Qual o cpf manzinho ?: ")
                        conta = cs.Poupanca(dianiver,nConta,cpf,0,True)
                        dados = (nConta, cpf, 0, dianiver)
                        P1 = cs.Poupanca(dianiver,nConta,cpf,0,True)
                        cursor.execute(f"INSERT INTO poupanca (numero, cpf,saldo,dia_aniversario) values({nConta},{cpf}, {conta.Saldo}, {dianiver})")
                        conexao.commit()
                    elif opof == "L":
                        opnum = input("Qual o numero da sua conta?: ")
                        cursor.execute("select * from Poupanca where numero = %s limit 1",opnum)
                        data = cursor.fetchall()
                        if len(data) > 0:
                            print("Achei sua conta!")
                            P1 = cs.Poupanca(data[0][4],data[0][1],data[0][2],data[0][3],True)
                            wah = True
                        else:
                            print("Não achei")
    global C1
    while wah:
        if(op == 2):
                if C1.Numero != None:
                    conta = C1
                    for i in range(10):
                        print(f"Saldo atual:{conta.Saldo} Talões : {conta.NTalao} Numero : {conta.Numero}")
                        print("Movimentos: C para Credito D para Debito")
                        wa = input("Digite: ")
                        if(wa == "C"):
                                C = int(input("digite o valor: "))
                                conta.Credito(C)
                                salso = (conta.Saldo, nConta)
                                cursor.execute("UPDATE corrente SET saldo = %s where numero = %s",salso )
                                conexao.commit()
                                i = i - 1 
                        elif(wa == "D"):
                                D = int(input("Digite o valor: "))
                                salso = (conta.Saldo, nConta)
                                cursor.execute("UPDATE corrente SET saldo = %s where numero = %s",salso )
                                conexao.commit()
                                conta.Debito(D)
                                i = i - 1
                        else:
                                break
                    dia = input("Você quer pegar um talão?: ")
                    if dia == "S":
                        conta.Talao()
                        salso = (conta.Saldo, nConta)
                        cursor.execute("UPDATE corrente SET saldo = %s where numero = %s",salso )
                        conexao.commit()
                        print("Seu saldo final : {conta.Saldo}")
                    else:
                        print('nah')
                else:
                        opof = input("não encontrei sua conta,  Quer tentar criar uma nova ? (C) ou tentar logar ? (L): ")
                        if opof == "C":  
                            nConta = random.randint(1,99999)
                            cpf = input("Qual o cpf manzinho ?: ")
                            conta = cs.Corrente(nConta,cpf,0,True,3)
                            dados = (nConta, cpf, 0)
                            C1 = cs.Corrente(nConta,cpf,0,True,3)
                            cursor.execute(f"INSERT INTO corrente (numero, cpf,saldo,ntalao) values({nConta},{cpf}, {conta.Saldo}, {conta.NTalao})")
                            conexao.commit()
                        elif opof == "L":
                            opnum = input("Qual o numero da sua conta?: ")
                            cursor.execute("select * from corrente where numero = %s limit 1",opnum)
                            data = cursor.fetchall()
                            if len(data) > 0:
                                print("Achei sua conta!")
                                C1 = cs.Corrente(data[0][4],data[0][1],data[0][2],data[0][3],True)
                                wah = True
                            else:
                                print("Não achei")
                


    global E1
    if(op == 3):
        if E1.Numero != None:
            conta = E1
            for i in range(10):
                print(f"Saldo atual:{conta.Saldo} Limite : {conta.Limite}")
                print("Movimentos: C para Credito D para Debito")
                wa = input("Digite: ")
                if(wa == "C"):
                    C = int(input("digite o valor: "))
                    conta.Credito(C)
                    salso = (conta.Saldo, conta.Limite, nConta )
                    cursor.execute("UPDATE especial SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()

                    i = i - 1 
                elif(wa == "D"):
                    D = int(input("Digite o valor: "))
                    conta.Debito(D)
                    salso = (conta.Saldo, conta.Limite, nConta )
                    cursor.execute("UPDATE especial SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()

                    i = i - 1
                else:
                    sair = True
                    break
        else:
            opof = input("não encontrei sua conta,  Quer tentar criar uma nova ? (C) ou tentar logar ? (L): ")
            if opof == "C":  
                nConta = random.randint(1,99999)
                cpf = input("Qual o cpf manzinho ?: ")
                conta = cs.Especial(1000,nConta,cpf,0,True)
                cursor.execute(f"INSERT INTO especial (numero, cpf,saldo,limite) values({conta.Numero},{cpf}, {conta.Saldo}, {conta.Limite})")
                conexao.commit()
            elif opof == "L":
                opnum = input("Qual o numero da sua conta?: ")
                cursor.execute("select * from corrente where numero = %s limit 1",opnum)
                data = cursor.fetchall()
                if len(data) > 0:
                    print("Achei sua conta!")
                    P1 = cs.Poupanca(data[0][4],data[0][1],data[0][2],data[0][3],True)
                    
            else:
                print("Não achei")
            
    if( op == 4):
        nConta = random.randint(1,99999)
        cpf = input("Qual o cpf manzinho ?: ")
        conta = cs.Empresa(nConta,cpf,0,True, 10000)
        cursor.execute(f"INSERT INTO empresa (numero, cpf,saldo,limite) values({nConta},{cpf}, {conta.Saldo}, {conta.LimEmpresitmo})")
        conexao.commit()
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo}, Emprestimo {conta.LimEmpresitmo}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                salso = (conta.Saldo, conta.LimEmpresitmo, nConta )
                cursor.execute("UPDATE empresa SET saldo = %s, limite = %s where numero = %s",salso )
                conexao.commit()

                i = i - 1 
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
                    salso = (conta.Saldo, conta.LimEmpresitmo, nConta )
                    cursor.execute("UPDATE empresa SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()

            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                if conta.Saldo < 0 :
                    conta.Emprestimo(D)
                    salso = (conta.Saldo, conta.LimEmpresitmo, nConta )
                    cursor.execute("UPDATE empresa SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()
                i = i - 1
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
                    salso = (conta.Saldo, conta.LimEmpresitmo, nConta )
                    cursor.execute("UPDATE empresa SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()
            else:
                break
    if(op == 5):
        nConta = random.randint(1,99999)
        cpf = input("Qual o cpf manzinho ?: ")
        conta = cs.Estudantil(nConta,cpf,0,True, 5000)
        cursor.execute(f"INSERT INTO estudantil (numero, cpf,saldo,limite) values({nConta},{cpf}, {conta.Saldo}, {conta.Limiteimite})")
        conexao.commit()
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo}, Limite {conta.Limiteimite}")
            print("Movimentos: C para Credito D para Debito")
            wa = input("Digite: ")
            if(wa == "C"):
                C = int(input("digite o valor: "))
                conta.Credito(C)
                salso = (conta.Saldo, conta.Limiteimite, nConta )
                cursor.execute("UPDATE estudantil SET saldo = %s, limite = %s where numero = %s",salso )
                conexao.commit()


                i = i - 1 
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
            elif(wa == "D"):
                D = int(input("Digite o valor: "))
                conta.Debito(D)
                salso = (conta.Saldo, conta.Limiteimite, nConta )
                cursor.execute("UPDATE estudantil SET saldo = %s, limite = %s where numero = %s",salso )
                conexao.commit()


                i = i - 1
                emp = input("Voce quer um emprestimo ?????: ")
                if(emp == "S"):
                    qnt = int(input("quanto: "))
                    conta.Emprestimo(qnt)
                    salso = (conta.Saldo, conta.Limiteimite, nConta )
                    cursor.execute("UPDATE estudantil SET saldo = %s, limite = %s where numero = %s",salso )
                    conexao.commit()
            else:
                break
    if(op == 6):
        print("ta bom xau")
        
        sair = True
        
if sair == True:
    print("gOOD BYE")
else:
    MainMenu()

#fechar conexão
conexao.close()