import pymysql
import os

def limpatela():
    os.system('cls')

conexao = pymysql.connect(
    host='localhost',
    user="root",
    password="fbradesco",
    database='agenda'
)

cursor = conexao.cursor()


cursor.execute("SELECT * FROM usuarios")

resultados =  cursor.fetchall()

print(resultados)


#inserir dados
dados = ("waow", "ohno@gmail.com", "11 9888-8888", "they took me and inserted me using they python")

cursor.execute("INSERT INTO usuarios (nome, email,telefone,mensagem) values(%s,%s,%s,%s)",dados)

conexao.commit()

cursor.execute("SELECT * FROM usuarios")

resultados =  cursor.fetchall()

print(resultados)

#fechar conexão
conexao.close()

