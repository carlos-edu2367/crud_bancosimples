
# Descrição do Projeto
Este projeto consiste em um sistema simples de gerenciamento de contas bancárias, com funcionalidades de login, cadastro de usuários e operações bancárias como saque, depósito e verificação de saldo. Ele foi desenvolvido utilizando Tkinter para a interface gráfica e SQLite para armazenamento de dados. O código é modularizado, utilizando uma camada de lógica em um arquivo externo chamado funcoesLogic, o que facilita a manutenção e escalabilidade do sistema.

# Tecnologias Utilizadas
Tkinter: Biblioteca para a criação da interface gráfica.
SQLite: Banco de dados relacional utilizado para armazenar os dados dos usuários e suas transações.
Python: Linguagem de programação principal utilizada no projeto.

# Como Rodar o Projeto
Pré-requisitos
Antes de rodar o projeto, certifique-se de ter o Python 3.x instalado em sua máquina. Você pode baixar o Python no site oficial.

Além disso, você precisa garantir que as bibliotecas necessárias estão instaladas. Caso não tenha o tkinter ou sqlite3, instale utilizando o seguinte comando:

bash
pip install tk sqlite3

# Passo a Passo para Executar
Baixe o código fonte

Faça o download ou clone este repositório para sua máquina. 
O código principal está no arquivo main.py, e o arquivo que contém as funções de lógica é o funcoesLogic.py.


# Rodando o Código

Navegue até o diretório do projeto no terminal e execute o seguinte comando:

bash
python main.py

# Primeiros Passos no Sistema

Ao rodar o código, a interface gráfica será carregada. Você verá duas opções principais:

Login: Para fazer login com um usuário previamente cadastrado.
Cadastrar: Para criar um novo usuário.
Após o login bem-sucedido, você terá acesso às opções de verificar saldo, sacar, depositar e deletar conta.

Caso não esteja logado, apenas as opções de Login e Cadastro estarão disponíveis.

# Funcionalidades Implementadas
Cadastro de Usuário: O usuário pode se cadastrar com um nome, e-mail e senha. O sistema valida a unicidade do e-mail, impedindo que um e-mail já registrado seja utilizado novamente.

Login de Usuário: O sistema autentica o usuário com base no e-mail e senha, permitindo o acesso às funcionalidades bancárias.

Operações Bancárias: Uma vez logado, o usuário pode realizar operações bancárias como:

Verificar saldo.
Realizar saque.
Realizar depósito.
Deletar conta.
Validação de Erros: O sistema trata diversos tipos de erros, como valores inválidos para operações de saque e depósito, e e-mails já cadastrados.

# Habilidades Desenvolvidas
Este projeto demonstrou minhas habilidades em várias áreas do desenvolvimento de software:

Desenvolvimento de Interfaces Gráficas: Utilizando Tkinter para criar uma interface amigável e intuitiva para o usuário.
Manipulação de Banco de Dados: Uso de SQLite para gerenciar o armazenamento de dados de usuários, garantindo persistência das informações.
Lógica de Programação: Implementação de funções para realizar login, cadastro e operações bancárias, com validação de entrada e tratamento de erros.
Boas Práticas de Programação: Modularização do código com a separação da lógica do sistema em um arquivo de funções externas (funcoesLogic.py), o que facilita a manutenção e escalabilidade.
Experiência com Python: Desenvolvimento de um projeto complexo utilizando a linguagem Python, com foco em programação orientada a objetos e integração com banco de dados.

# Contribuições e Melhorias Futuras
Criação de Testes Automatizados: Implementação de testes unitários para garantir a integridade do código.
Aprimoramento da Interface: Melhoria na interface gráfica para torná-la mais moderna e responsiva.
Integração com outros Bancos de Dados: Adicionar suporte para outros sistemas de banco de dados, como PostgreSQL, para maior escalabilidade.

# Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
