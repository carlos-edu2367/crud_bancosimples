import sqlite3
import tkinter as tk


def inicializar():
    try:
        conexao = sqlite3.connect("banco_de_dados.db")

        cursor = conexao.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
            )
        """)
        
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS saldos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL UNIQUE,
                        saldo REAL
                    )
                    """)

        conexao.commit()

        conexao.close()

        
        
    except sqlite3.Error as e:
        print("ERRO: ", e)

    else:
        print("Banco de dados criado / conectado com sucesso")


global id
id = 0

def cadastrarUsu(nome, email, senha):
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    # Insere os dados do usuário no banco
    cursor.execute("""
                   INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)
                   """, (nome, email, senha))
    conexao.commit()
    
    # Inicializa o saldo do usuário
    cursor.execute("""
                   INSERT INTO saldos (email, saldo) VALUES (?, ?)
                   """, (email, 0))
    conexao.commit()
    
    conexao.close()
    return True

import sqlite3

def validarUsu(email, senha):
    try:
        # Conecta ao banco de dados
        conexao = sqlite3.connect("banco_de_dados.db")
        cursor = conexao.cursor()

        # Consulta a senha com base no email
        cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
        resultado = cursor.fetchone()

        # Verifica se encontrou algum resultado
        if resultado:
            senha_armazenada = resultado[0]

            # Compara a senha fornecida com a armazenada
            if senha_armazenada == senha:
                # Obtém o ID do usuário
                cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
                ident = cursor.fetchone()

                conexao.close()
                return ident[0]  # Retorna o ID do usuário em caso de sucesso
        # Caso senha ou email estejam incorretos
        conexao.close()
        return False
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        return False


def verificarSaldo(cod):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    cursor.execute("""
                   SELECT saldo FROM saldos WHERE id = ?
                   """, (cod,))
    saldo = cursor.fetchone()  # Chamada correta do método
    conexao.commit()
    conexao.close()
    # Retorna o saldo ou 0 se o saldo não existir
    return saldo[0] if saldo else 0


def adicionarSaldo(cod, value):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    saldo = verificarSaldo(cod)
    novoSaldo = saldo+value
    cursor.execute("""
                       UPDATE saldos
                       SET saldo = ?
                       WHERE id = ?
                       """, (novoSaldo, cod))
    conexao.commit()
    conexao.close()


def sacarSaldo(code, value):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    saldo = verificarSaldo(code)
    if value <= saldo:
        novoSaldo = saldo - value
        cursor.execute("""
                       UPDATE saldos
                       SET saldo = ?
                       WHERE id = ?
                       """, (novoSaldo, code))
        conexao.commit()
        conexao.close()
        return True
    else:
        conexao.close()
        return False
    

def delet_user(id):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    cursor.execute("DELETE FROM saldos WHERE id = ?", (id,))

    
    conexao.commit()
    conexao.close()