import sqlite3



def cadastrarUsu(nome, email, senha):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    
    cursor.execute("""
                   INSERT INTO usuarios( nome, email, senha) VALUES(?, ?, ?)
                   """, (nome, email, senha))
    conexao.commit()
    cursor.execute("""
                   INSERT INTO saldos (email, saldo) VALUES(?, ?)
                   """, (email, 0))
    conexao.commit()

    conexao.close()



def validarUsu(email, senha):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    cursor.execute(""" 
                   SELECT senha FROM usuarios WHERE email = (?)
                   """, (email,))
    resultado = cursor.fetchone()

    conexao.commit()
    if resultado:
        senha_armazenada = resultado[0]
        if senha_armazenada == senha:
            cursor.execute("""
                           SELECT id FROM usuarios WHERE email = ?
                           """, (email,))
            ident = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return ident[0]
            
        else:
            conexao.close()
            return False
    else:
        conexao.close()
        return False
    


def verificarSaldo(cod):
    conexao = sqlite3.connect("banco_de_dados.db")

    cursor = conexao.cursor()
    cursor.execute("""
                   SELECT saldo FROM saldos WHERE id = ?
                   """, (cod,))
    saldo = cursor.fetchone()  # Chamada correta do método
    conexao.commit()
    # Retorna o saldo ou 0 se o saldo não existir
    conexao.close()
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


def main():
    id = 0
    opt = 15
    while True:
        if id == 0:
            opt = int(input("1 - LOGIN      2 - CADASTRO     0 - SAIR:   "))
            match opt:
                case 1:
                    email = input("EMAIL: ")
                    senha = input("SENHA: ")
                    try:
                        id = validarUsu(email, senha)

                    except False:
                        print("Usuário ou senha incorretos.")
                case 2:
                    name = input("NOME: ")
                    email = input("EMAIL: ")
                    senha = input("SENHA: ")

                    sit = cadastrarUsu(name, email, senha)
                    if sit == False:
                        print("Usuário ou senha inválidos.")
                    id = validarUsu(email, senha)
        else:
            opt = int(
                input("1 - VERIFICAR SALDO      2 - ADICIONAR SALDO  3- SACAR    0 - SAIR:   "))

            match opt:
                case 1:
                    saldo = verificarSaldo(id)
                    print(f"SEU SALDO É: {saldo}")

                case 2:
                    valor = float(input("Quanto deseja depositar?  "))
                    adicionarSaldo(id, valor)

                case 3:
                    valor = float(input("Quanto deseja sacar?  "))
                    res = sacarSaldo(id, valor)
                    if res == False:
                        print("Valor indisponível")
                    else:
                        print("Saque realizado com sucesso! ")
        if opt == 0:
            break


main()

