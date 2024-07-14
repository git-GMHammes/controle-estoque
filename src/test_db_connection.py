import pymysql
import os

# Configurações de conexão usando variáveis de ambiente
DB_USER = os.getenv('DB_USER', 'root')
DB_PASS = os.getenv('DB_PASS', 'pass_root')
DB_NAME = os.getenv('DB_NAME', 'db')
DB_HOST = os.getenv('DB_HOST', 'mysql-db')

# Tentar se conectar ao banco de dados
try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    print("Conexão com o banco de dados estabelecida com sucesso!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
