import mysql.connector
from mysql.connector import Error

#============= CRIAÇÃO DE UAM AGENDA EM PYTHON CONECTADO AO MYSQL =============#
#ESTABELECE A CONEXÃO COM O BANCO DE DADOS
def conectar():
    global conexao
    global cursor
    try:
        conexao = mysql.connector.connect(
        host='localhost',
        database='db_pratica_integradora',
        user='root',
        password='***********',
        auth_plugin = 'mysql_native_password')
        print("Conectado...")
    except Error as erro:
        print(erro)

#CRIA TABELA
def criar_tabela():
    try:
        conectar()
        criar = """CREATE TABLE IF NOT EXISTS tbl_contatos( 
                IDContato int(10) NOT NULL,
                Nome varchar(70) NOT NULL,
                Telefone varchar(30) NOT NULL,
                Email varchar(30) NOT NULL,
                Endereco varchar(100) NOT NULL,
                PRIMARY KEY (IDContato))
                """
        cursor = conexao.cursor()
        cursor.execute(criar)
        print("Tabela criada com sucesso!")
    except Error as erro:
        print(erro)

#RECEBE DADOS DO USUÁRIO PARA INSERIR NA TABELA
def inserir_dados():
    ident = input("Insira o id do contato: ")
    nome = input("Insira o nome do contato: ")
    telefone = input("Insira o telefone: ")
    email = input("Insira o email: ")
    endereco = input("Insira o endereço do contato: ")

    try:
        conectar()
        inserir = f'''INSERT INTO tbl_contatos
                       (IDContato, Nome, Telefone, Email, Endereco)
                       VALUES  
                       ({ident}, '{nome}', '{telefone}', '{email}', '{endereco}')    
                '''
        cursor = conexao.cursor()
        cursor.execute(inserir)
        conexao.commit()
        print("Dados inseridos")
        print(f"Quantidade de linhas inseridas: {cursor.rowcount}")
    except Error as erro:
        print(erro)

#EXIBE TODOS OS DADOS DA TABELA
def mostrar_contatos():
    try:
        conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tbl_contatos")
        consulta = cursor.fetchall()
        print("=============== MEUS CONTATOS ===============")
        for linha in consulta:
            print("ID: ", linha[0])
            print("Nome: ", linha[1])
            print("Telefone: ", linha[2])
            print("Email: ",linha[3])
            print("Endereço: ",linha[4])
            print("*******************************")
    except Error as erro:
        print(erro)


#PESQUISA CONTATO POR NOME E RETORNA OS DADOS
def pesquisar_contatos():

    nome_procurado = input("Insira o nome a ser procurado em sua agenda: ")
    try:
        conectar()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM tbl_contatos WHERE Nome = {nome_procurado}")
        consulta = cursor.fetchall()
        for linha in consulta:
            print("ID: ", linha[0])
            print("Nome: ", linha[1])
            print("Telefone: ", linha[2])
            print("Email: ", linha[3])
            print("Endereço: ", linha[4])

    except Error as erro:
        print("Não encontrado!")

#REMOVE UM CONTATO DA AGENDA
def remover_contato():

    try:
        conectar()
        cursor = conexao.cursor()
        nome_procurado = input("Insira o nome do contato que quer remover obs: precisar ser entre aspas simples 'NOME': ")
        cursor.execute(f"DELETE FROM tbl_contatos WHERE Nome = {nome_procurado}")
        comando = cursor.fetchall()
        print(f"Contato {nome_procurado} removido com sucesso!")
        print(f"{cursor.rowcount} linha removida da tabela")
    except Error as erro:
        print("Operação falhou!")

#ALTERAR REGISTROS DA TABELA
def alterar_contato():

    try:
        conectar()
        cursor = conexao.cursor()
        nome_procurado = input("Insira o nome do contato que quer alterar obs: precisar ser entre aspas simples exemplo 'NOME': ")
        print("**** MENU ALTERAÇÃO DE DADOS ****")
        opc = int(input("[1] ALTERAR NOME\n[2] ALTERAR TELEFONE\n[3] ALTERAR EMAIL\n[4] ALTERAR ID\n[5] ALTERAR ENDEREÇO\n[0] SAIR\nInsira uma opção: "))

        if opc == 1:
            novo_nome = input("Insira o novo nome: ")
            cursor.execute(f"UPDATE tbl_contatos SET Nome = {novo_nome} WHERE Nome = {nome_procurado}")
            conexao.commit()
            print(f"Contato {nome_procurado} alterado com sucesso!")
            print(f"Linhas afetadas: {cursor.rowcount}")

        elif opc == 2:
            novo_telefone = input("Insira o novo telefone: ")
            cursor.execute(f"UPDATE tbl_contatos SET Telefone = {novo_telefone} WHERE Nome = {nome_procurado}")
            conexao.commit()
            print(f"Contato {nome_procurado} alterado com sucesso!")
            print(f"Linhas afetadas: {cursor.rowcount}")

        elif opc == 3:
            novo_email = input("Insira o novo email: ")
            cursor.execute(f"UPDATE tbl_contatos SET Email = {novo_email} WHERE Nome = {nome_procurado}")
            conexao.commit()
            print(f"Contato {nome_procurado} alterado com sucesso!")
            print(f"Linhas afetadas: {cursor.rowcount}")

        elif opc == 4:
            novo_id = input("Insira o novo ID: ")
            cursor.execute(f"UPDATE tbl_contatos SET IDContato = {novo_id} WHERE Nome = {nome_procurado}")

        elif opc == 5:
            novo_end = input("Insira o novo endereço: ")
            cursor.execute(f"UPDATE dbl_contatos SET Endereco = {novo_end} WHERE Nome = {nome_procurado}")

        else:
            print("Opção inválida!")

    except Error as erro:
        print("Falha ao alterar dados!")

#ENCERRAR CONEXÃO COM O BANCO DE DADOS
def encerrar():

    cursor = conexao.cursor()
    conexao.close()
    cursor.close()
    print("Desconectando do banco...")

#================ PROGRAMA PRINCIPAL -===============#

booleano = False

while(booleano == False):
    opc = int(input("***** MENU ***** "
                    "\n[1] - INSERIR"
                    "\n[2] - EXIBIR LISTA"
                    "\n[3] - REMOVER"
                    "\n[4] - PROCURAR CONTATO"
                    "\n[5] - ALTERAR CONTATO"
                    "\n[0] - SAIR"
                    "\nINSIRA UMA OPÇÃO: "))

    if opc == 1:
        inserir_dados()

    elif opc == 2:
        mostrar_contatos()

    elif opc == 3:
        remover_contato()

    elif opc == 4:
        pesquisar_contatos()

    elif opc == 5:
        alterar_contato()

    elif opc == 0:
        encerrar()
        booleano = True

    else:
        print("OPÇÃO INVÁLIDA!")
