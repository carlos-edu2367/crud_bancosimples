import sqlite3


conexao = sqlite3.connect("banco_de_dados.db")

cursor = conexao.cursor()

cursor.execute("""DROP TABLE IF EXISTS usuarios""")
cursor.execute("""DROP TABLE IF EXISTS saldos""")
    
conexao.commit
conexao.close