import pymysql
import os
from classesTeste import Produti
import time
import random

def limpaTela():
    os.system('cls')

#criando banco de dados
con = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'fbradesco',
    database = 'yabadaba'
)

with con:
    with con.cursor() as cursor:
        TABLE_NAME = "produto"
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
                       'ID INT AUTO_INCREMENT PRIMARY KEY ,'
                       'CODIGO VARCHAR(50) ,'
                       'NOME VARCHAR(50) ,'
                       'VALOR DOUBLE(10,2) ,'
                       'ESTOQUE INT NOT NULL'      
        ')')
    with con.cursor() as cursor:
        while True:

            print("1 - Cadastrar")
            print("2 - Alterar")
            print("3 - Listar")
            print("4 - Excluir")
            print("5 - Movimento")
            print("6 - Sair")

            op  = input('Escolha o numero: ')
            if op == '6':

                time.sleep(2)
                print("byeeeee")
                break

            elif op == '1':

                #Cadastrar
                time.sleep(2)
                print('Cadastro')
                codigo = random.randint(0,99999)
                nome = input("Nome: ")
                valor = float(input("Digite o valor: "))
                item = Produti(None,codigo,nome,valor,0)
                cursor.execute('INSERT INTO PRODUTO(CODIGO,NOME,VALOR,ESTOQUE)'\
                'VALUES (%s,%s,%s,%s)', (item.codigo,item.nome,item.valor, item.estoque))
                con.commit()

            elif op == '2':

                #Alterar
                print("- " * 20)
                print("ALTERAÇÃO")
                codigo = input("insira o código do produto: ")
                cursor.execute('SELECT * FROM PRODUTO WHERE CODIGO = %s', codigo)
                dado = cursor.fetchall()
                if len(dado) > 0:
                    for x in dado:
                        print("ID  CÓDIGO   NOME   VALOR  ESTOQUE")
                        print(x)
                    nome = input('Digite o Novo nome: ')
                    valor = float(input("Digite o valor novo : "))
                    item = Produti(None,codigo,nome,valor,0)
                    cursor.execute('UPDATE PRODUTO SET NOME = %s, VALOR = %s  WHERE CODIGO = %s',(item.nome, item.valor, item.codigo))
                    con.commit()



            elif op == '3':

                #Listar
                print("- " *20)
                print("LISTAGEM")
                cursor.execute('SELECT * FROM produto')
                resposta = cursor.fetchall()
                if len(resposta) == 0:
                    print('Não tem nada')
                else:
                    for x in resposta:
                        print("ID  CÓDIGO   NOME   VALOR  ESTOQUE")
                        print(x)

            elif op == '4':

                #Excluir
                print("- " * 20)
                print("DELETAR")
                cursor.execute('SELECT * FROM PRODUTO')
                dado = cursor.fetchall()
                if len(dado) > 0:
                    for x in dado:
                        print("ID  CÓDIGO   NOME   VALOR  ESTOQUE")
                        print(x)
                codigo = input("insira o código do para deletar: ")
                cursor.execute('DELETE FROM PRODUTO WHERE CODIGO = %s',(codigo))
                con.commit()

            elif op == '5':
                #Movimentos
                print('- '* 20)
                codigo = print('digite o codigo do produto a ser movimentado: ')
                cursor.execute('SELECT * FROM PRODUTO WHERE CODIGO = %s',(codigo))
                item= cursor.fetchall()
                Produti_item = Produti(*item)
                print(Produti_item)

            