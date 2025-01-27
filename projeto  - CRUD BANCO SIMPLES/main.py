import tkinter as tk
import sqlite3
import funcoesLogic
from tkinter import messagebox

root = tk.Tk()
root.title("Banco CRUD Simples")

# Variável para armazenar o ID do usuário logado
user_id = None

funcoesLogic.inicializar()


def warning(erro_type):
    tela_erro = tk.Toplevel()
    tela_erro.title("Erro")

    erro = tk.Label(f"ERRO: {erro_type}")
    erro.pack(pady=10)


def abrir_tela_login():
    # Criando a janela de login como janela secundária
    login_window = tk.Toplevel()
    login_window.title("Tela de Login")
    login_window.geometry("300x200")

    # Função chamada ao clicar no botão "Entrar"
    def realizar_login():
        global user_id
        email = entry_email.get()  # Obtém o texto do campo de email
        senha = entry_senha.get()  # Obtém o texto do campo de senha

        # Chama a função validarUsu da lógica e verifica o resultado
        user_id = funcoesLogic.validarUsu(email, senha)
        if user_id:  # Se o retorno for um ID válido
            messagebox.showinfo(
                "Login", f"Login realizado com sucesso! ID: {user_id}")
            login_window.destroy()  # Fecha a janela de login
            atualizar_tela_principal()  # Atualiza a tela principal com os botões de login
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos!")

    # Criando os widgets da tela de login
    tk.Label(login_window, text="Email:").pack(pady=5)
    entry_email = tk.Entry(login_window, width=30)
    entry_email.pack(pady=5)

    tk.Label(login_window, text="Senha:").pack(pady=5)
    # Campo para senha (oculta os caracteres)
    entry_senha = tk.Entry(login_window, width=30, show="*")
    entry_senha.pack(pady=5)

    # Botão para tentar o login
    tk.Button(login_window, text="Entrar",
              command=realizar_login).pack(pady=10)


def abrir_tela_cadastro():
    # Criando a janela de cadastro
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Tela de Cadastro")
    cadastro_window.geometry("400x300")

    # Função chamada ao clicar no botão "Cadastrar"
    def realizar_cadastro():
        nome = entry_nome.get()  # Obtém o nome
        email = entry_email.get()  # Obtém o email
        senha = entry_senha.get()  # Obtém a senha

        # Valida se todos os campos foram preenchidos
        if not nome or not email or not senha:
            messagebox.showerror(
                "Erro", "Todos os campos devem ser preenchidos!")
            return

        # Chama a função de lógica para cadastrar o usuário
        try:
            if funcoesLogic.cadastrarUsu(nome, email, senha):
                messagebox.showinfo(
                    "Sucesso", "Usuário cadastrado com sucesso!")
                cadastro_window.destroy()  # Fecha a janela de cadastro
            else:
                messagebox.showerror(
                    "Erro", "Ocorreu um erro ao cadastrar o usuário!")
        except sqlite3.IntegrityError as e:
            # Tratamento para duplicidade de email
            messagebox.showerror("Erro", "O email já está cadastrado!")
        except Exception as e:
            # Qualquer outro erro
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    # Criando os widgets da tela de cadastro
    tk.Label(cadastro_window, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(cadastro_window, width=40)
    entry_nome.pack(pady=5)

    tk.Label(cadastro_window, text="Email:").pack(pady=5)
    entry_email = tk.Entry(cadastro_window, width=40)
    entry_email.pack(pady=5)

    tk.Label(cadastro_window, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(cadastro_window, width=40,
                           show="*")  # Campo para senha
    entry_senha.pack(pady=5)

    # Botão para cadastrar
    tk.Button(cadastro_window, text="Cadastrar",
              command=realizar_cadastro).pack(pady=20)


def atualizar_tela_principal():
    """Atualiza a tela principal de acordo com o estado de login"""
    if user_id:  # Se o usuário estiver logado
        # Exibe os botões principais
        for widget in frame_principal.winfo_children():
            widget.destroy()  # Remove os widgets anteriores

        tk.Button(frame_principal, text="Verificar Saldo",
                  width=20, command=verificar_saldo).pack(pady=5)
        tk.Button(frame_principal, text="Sacar",
                  width=20, command=sacar).pack(pady=5)
        tk.Button(frame_principal, text="Depositar",
                  width=20, command=depositar).pack(pady=5)
        tk.Button(frame_principal, text="Deletar Conta",
                  width=20, command=deletar_conta).pack(pady=5)
        tk.Button(frame_principal, text="Sair",
                  width=20, command=sair).pack(pady=5)

    else:  # Se o usuário não estiver logado
        # Exibe os botões de login e cadastro
        for widget in frame_principal.winfo_children():
            widget.destroy()  # Remove os widgets anteriores

        tk.Button(frame_principal, text="Login", width=20,
                  command=abrir_tela_login).pack(pady=5)
        tk.Button(frame_principal, text="Cadastrar", width=20,
                  command=abrir_tela_cadastro).pack(pady=5)


def verificar_saldo():
    """Exibe o saldo do usuário logado"""
    if user_id:
        saldo = funcoesLogic.verificarSaldo(user_id)
        messagebox.showinfo("Saldo", f"Seu saldo é: R${saldo:.2f}")
    else:
        messagebox.showerror(
            "Erro", "Você precisa estar logado para verificar o saldo!")


def sacar():
    """Abre uma tela para sacar o saldo"""
    def realizar_saque():
        try:
            valor = float(entry_valor.get())
            if valor <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que 0!")
                return
            if funcoesLogic.sacarSaldo(user_id, valor):
                messagebox.showinfo("Sucesso", f"Saque de R${
                                    valor:.2f} realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            saque_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido!")

    # Criando a janela de saque
    saque_window = tk.Toplevel()
    saque_window.title("Tela de Saque")
    saque_window.geometry("300x150")

    tk.Label(saque_window, text="Valor do saque:").pack(pady=10)
    entry_valor = tk.Entry(saque_window, width=20)
    entry_valor.pack(pady=5)

    tk.Button(saque_window, text="Realizar Saque",
              command=realizar_saque).pack(pady=10)


def depositar():
    """Abre uma tela para depositar o valor"""
    def realizar_deposito():
        try:
            valor = float(entry_valor.get())
            if valor <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que 0!")
                return
            funcoesLogic.adicionarSaldo(user_id, valor)
            messagebox.showinfo("Sucesso", f"Depósito de R${
                                valor:.2f} realizado com sucesso!")
            deposito_window.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido!")

    # Criando a janela de depósito
    deposito_window = tk.Toplevel()
    deposito_window.title("Tela de Depósito")
    deposito_window.geometry("300x150")

    tk.Label(deposito_window, text="Valor do depósito:").pack(pady=10)
    entry_valor = tk.Entry(deposito_window, width=20)
    entry_valor.pack(pady=5)

    tk.Button(deposito_window, text="Realizar Depósito",
              command=realizar_deposito).pack(pady=10)


def deletar_conta():
    """Função para deletar a conta do usuário"""
    if user_id:
        resposta = messagebox.askyesno(
            "Confirmar", "Você tem certeza de que deseja deletar sua conta?")
        if resposta:  # Se o usuário confirmar a exclusão
            funcoesLogic.delet_user(user_id)
            messagebox.showinfo(
                "Sucesso", "Sua conta foi deletada com sucesso!")
            sair()  # Desloga o usuário após deletar a conta
    else:
        messagebox.showerror(
            "Erro", "Você precisa estar logado para deletar sua conta!")


def sair():
    """Função para fazer logout"""
    global user_id
    user_id = None  # Limpa o ID do usuário
    atualizar_tela_principal()  # Atualiza a tela principal


# Frame principal onde os botões serão exibidos
frame_principal = tk.Frame(root)
frame_principal.pack(padx=10, pady=10)

# Atualiza a tela inicial
atualizar_tela_principal()

root.mainloop()
