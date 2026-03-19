import os
import mysql.connector
from dotenv import load_dotenv

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
password=os.getenv("Senha_Banco"),
database="bd01",

)

cursor = conexao.cursor()

#CRUD
nome_produto = "Lapis"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" ' #Texto MySQl precisa estar entre ""
cursor.execute(comando)
conexao.commit() #edita o banco de dados


cursor.close()
conexao.close()

#CREATE

#nome_produto = "Lapis"
#valor = 5
#comando = f'INSERT INTO vendas (nome_produto, valor ) VALUES ("{nome_produto}",{valor})'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#READ

# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# #conexao.commit() #edita o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados
# print(resultado)

#UPDATE

# nome_produto = "Lapis"
# valor = 7
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" ' #Texto MySQl precisa estar entre ""
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados

#DELETE

# nome_produto = "Lapis"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" ' #Texto MySQl precisa estar entre ""
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados


