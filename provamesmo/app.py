import pymysql
import os
import EletricClasses as EC
import time
import random

def limpaTela():
    os.system('cls')

#criando banco de dados
con = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'fbradesco',
    database='eletronicosplus'
)

#create database : 
#con.cursor().execute('CREATE DATABASE eletronicosplus ')
with con:
    with con.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS usuario (ID INT AUTO_INCREMENT PRIMARY KEY, EMAIL VARCHAR(50),SENHA VARCHAR(50))')
        cursor.execute('CREATE TABLE IF NOT EXISTS produtoeletronico (id_produtoeletronico INT AUTO_INCREMENT PRIMARY KEY ,descricao VARCHAR(50) ,marca VARCHAR(50) ,valor DOUBLE(10,2),estoque int not null)')

def MainMenu():
    while True:
        print('1 - Cadastrar Produtos')
        print('2 - Cadastrar Usuario')
        print('3 - Sair')
        op = input('Digite o numero correspondente: ')
        if op == '3':
            print("ok goodbye")
            break
        elif op == '2':
            MenuUsuario()
        elif op == '1':
            MenuProdutos()


def MenuProdutos():
    con = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'fbradesco',
    database='eletronicosplus'
)
    

    with con.cursor() as cursor:
        while True:
            print('Loja Eletrônicos Plus')
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
                descricao = input("Digite a descrição do produto: ")
                marca = input("Digite a marca do produto: ")
                valor = float(input("Digite o valor: "))
                estoque = int(input('Digite o estoque: '))
                item = EC.ProdutoEletronico(None,descricao, marca,valor,estoque)
                dados = (item.descricao, item.marca, item.valor, item.estoque)
                cursor.execute('INSERT INTO produtoeletronico (descricao,marca,VALOR,ESTOQUE) VALUES (%s,%s,%s,%s)', dados)
                con.commit()

            elif op == '2':

                #Alterar
                print("- " * 20)
                print("ALTERAÇÃO")
                id = input("insira o código do produto: ")
                cursor.execute('SELECT * FROM produtoeletronico WHERE id_produtoeletronico = %s', id)
                dado = cursor.fetchall()
                if len(dado) > 0:
                    for x in dado:
                        print("ID  CÓDIGO   NOME   VALOR  ESTOQUE")
                        print(x)
                    nome = input('Digite a nova descrição: ')
                    marca = input('Digite a nova marca: ')
                    valor = float(input("Digite o valor novo : "))
                    estoque = int(input("Digite o estoque novo: "))
                    item = EC.ProdutoEletronico(None,nome,marca,valor,estoque)
                    cursor.execute('UPDATE produtoeletronico SET descricao = %s, marca = %s, valor = %s, estoque = %s  WHERE CODIGO = %s',(item.descricao, item.marca, item.valor, item.estoque))
                    con.commit()



            elif op == '3':

                #Listar
                print("- " *20)
                print("LISTAGEM")
                cursor.execute('SELECT * FROM produtoeletronico')
                resposta = cursor.fetchall()
                if len(resposta) == 0:
                    print('Não tem nada')
                else:
                    for x in resposta:
                        print("ID  DESCRIÇÃO   MARCA   VALOR  ESTOQUE")
                        print(x)

            elif op == '4':

                #Excluir
                print("- " * 20)
                print("DELETAR")
                cursor.execute('SELECT * FROM produtoeletronico')
                dado = cursor.fetchall()
                if len(dado) > 0:
                    for x in dado:
                        print("ID  CÓDIGO   NOME   VALOR  ESTOQUE")
                        print(x)
                codigo = input("insira o id do para deletar: ")
                cursor.execute('DELETE FROM produtoeletronico WHERE id_produtoeletronico = %s',(codigo))
                con.commit()

            elif op == '5':
                print(" 1 - Remover do estoque\n 2 - Adicionar no estoque")
                inpt = input("Digite o numero: ")
                if inpt == '1':
                    id = input("insira o ID do produto: ")
                    cursor.execute('SELECT * FROM produtoeletronico WHERE id_produtoeletronico = %s', id)
                    dado = cursor.fetchall()
                    if len(dado) > 0:
                        for x in dado:
                            print("ID  DESCRIÇÃO   MARCA   VALOR  ESTOQUE")
                            print(x)
                    item = EC.ProdutoEletronico(dado[0][0], dado[0][1], dado[0][2], dado[0][3],dado[0][4])
                    qtde = int(input("insira a quantidade pra remover: "))
                    item.Retirar(qtde)
                    cursor.execute('UPDATE produtoeletronico SET estoque =%s WHERE id_produtoeletronico = %s', (item.estoque, item.id_produtoeletronico))
                    con.commit()
                elif inpt == '2':
                    id = input("insira o ID do produto: ")
                    cursor.execute('SELECT * FROM produtoeletronico WHERE id_produtoeletronico = %s', id)
                    dado = cursor.fetchall()
                    if len(dado) > 0:
                        for x in dado:
                            print("ID  DESCRIÇÃO   MARCA   VALOR  ESTOQUE")
                            print(x)
                    item = EC.ProdutoEletronico(dado[0][0], dado[0][1], dado[0][2], dado[0][3],dado[0][4])
                    qtde = int(input("insira a quantidade pra adicionar: "))
                    item.Incluir(qtde)
                    cursor.execute('UPDATE produtoeletronico SET estoque =%s WHERE id_produtoeletronico = %s', (item.estoque, item.id_produtoeletronico))
                    con.commit()


def MenuUsuario():
    con = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'fbradesco',
    database='eletronicosplus'
)   
    finalPrice = 0
    with con.cursor() as cursor:
        cursor.execute('SELECT * FROM USUARIO')
        users = cursor.fetchall()
        usuarios = []
        if len(users) == 0:
            print('Loja Eletrônicos Plus')
            print("Inicie seu cadastro")
            email = input('Digite seu email: ')
            senha = input("Digite sua senha (nao se preocupe eh mt segura): ")
            dados = (email,senha)
            cursor.execute('INSERT INTO USUARIO (EMAIL, SENHA) Values (%s,%s)', dados)
            con.commit()
        else:
            print('Loja Eletrônicos Plus')
            print('Oi!')
            cursor.execute('SELECT * FROM USUARIO')
            users = cursor.fetchall()
            for x in users:
                usuarios.append(x)
            email = input("Digite seu Email: ")
            if usuarios:
                carrinho = []
                senha = input("Digite sua senha: ")
                #cursor.execute('SELECT * FROM USUARIO WHERE SENHA = %s', senha)
                print('Bem-vindo! a Eletrônicos Plus')
                print('1 - Incluir no carrinho')
                print('2 - Limpar Carrinho ')
                op = input('Insira o numero: ')
                if op == '1':
                    continuar = True
                    while continuar:
                        cursor.execute('SELECT * FROM produtoeletronico')
                        produtos = cursor.fetchall()
                        for x in produtos:
                            print(x)
                        prod_op = int(input('Escolha o id do produto: '))
                        cursor.execute('SELECT * FROM produtoeletronico where id_produtoeletronico = %s',prod_op)
                        dados = cursor.fetchall()
                        item = EC.ProdutoEletronico(dados[0][0], dados[0][1], dados[0][2], dados[0][3], dados[0][4])
                        if item.estoque > 0:
                            wah = (dados[0][0], dados[0][1], dados[0][2], dados[0][3], 1)
                            carrinho.append(wah)
                            print(carrinho)
                            op = input('continuar ?: ')
                            if op == 'S':
                                continuar = True
                            else:
                                continuar = False
                        else:
                            print('nao ta podendo')
                            continuar = True

                    print('Sua nota fiscal: ')
                    print(carrinho)
                    for x in carrinho:
                        id = x[0]
                        value = x[3]
                        finalPrice += value
                        cursor.execute('UPDATE produtoeletronico SET estoque = estoque - 1 WHERE id_produtoeletronico = %s',id )
                        con.commit()
                    print(f'preço final: {finalPrice} ')
                if op == '2':
                    print("Limpando carrinho...:")
                    carrinho = []
                    MenuUsuario()
                    


                
            else:
                print("Não te encontrei...")
   

MainMenu()
