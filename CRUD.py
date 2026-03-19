import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
password="Mycomputer",
database="bd01",

)

cursor = conexao.cursor()

comando = ''
cursor.execute(comando)


cursor.close()
conexao.close()
