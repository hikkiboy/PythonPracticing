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
        dianiver = int(input("Qual o seu aniversario ?: "))
        nConta = random.randint(1,99999)
        cpf = input("Qual o cpf manzinho ?: ")
        conta = cs.Poupanca(dianiver,nConta,cpf,0,True)
        dados = (nConta, cpf, 0, dianiver)
        cursor.execute(f"INSERT INTO poupanca (numero, cpf,saldo,dia_aniversario) values({nConta},{cpf}, {conta.Saldo}, {dianiver})")
        conexao.commit()

        if dianiver > 0: 
            for i in range(10):
                print(f"Saldo atual:{conta.Saldo} Dia aniversario : {conta.diaAniversario}")
                print("Movimentos: C para Credito D para Debito")
                
                wa = input("Digite: ")
                
                
                if(wa == "C"):
                    C = int(input("digite o valor: "))
                    conta.Credito(C)
                    salso = (conta.Saldo, nConta)
                    cursor.execute("UPDATE poupanca SET saldo = %s where numero = %s",salso )
                    conexao.commit()
                    i = i - 1 


                elif(wa == "D"):
                    D = int(input("Digite o valor: "))
                    conta.Debito(D)
                    salso = (conta.Saldo, nConta)
                    cursor.execute("UPDATE poupanca SET saldo = %s where numero = %s",salso )

                    conexao.commit()
                    i = i - 1


            
            dia = input("Que dia é hoje ?: ")
            if dia == dianiver:
                conta.Correcao(dia)
            else:
                print('nah')
        else:
            print("digita um numero valido e tenta denovo")
        

    elif(op == 2):
        conta = cs.Corrente(1,1,0,True,3)
        nConta = random.randint(1,99999)
        cpf = input("Qual o cpf manzinho ?: ")
        conta = cs.Corrente(nConta,cpf,0,True, 3)
        cursor.execute(f"INSERT INTO corrente (numero, cpf,saldo,nTalao) values({nConta},{cpf}, {conta.Saldo}, {conta.NTalao})")
        conexao.commit()

        
        for i in range(10):
            print(f"Saldo atual:{conta.Saldo} Talões : {conta.NTalao}")
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


    elif(op == 3):


        nConta = random.randint(1,99999)
        cpf = input("Qual o cpf manzinho ?: ")
        conta = cs.Especial(1000,nConta,cpf,0,True)
        cursor.execute(f"INSERT INTO especial (numero, cpf,saldo,limite) values({nConta},{cpf}, {conta.Saldo}, {conta.Limite})")
        conexao.commit()


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
    elif( op == 4):
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
    elif(op == 5):
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
    elif(op == 6):
        print("ta bom xau")
        
        sair = True
        
if sair == True:
    print("gOOD BYE")
else:
    MainMenu()

#fechar conexão
conexao.close()