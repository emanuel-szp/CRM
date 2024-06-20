# Importa o módulo mysql.connector
import mysql.connector

# Define a classe Registro
class Registro:
    # Define o construtor da classe Registro
    def __init__(self, nome, telefone, compra_passada):
        self.nome = nome
        self.telefone = telefone
        self.compra_passada = compra_passada

# Define a classe SistemaCRM
class SistemaCRM:
    # Define o construtor da classe SistemaCRM
    def __init__(self):
        # Estabelece a conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='he182555@',
            database='CRM'
        )
        # Cria um objeto cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()

    # Método para adicionar um registro
    def adicionar_registro(self, registro):
        # Define a instrução SQL para inserir os valores na tabela
        sql = 'INSERT INTO registro (nome, telefone, compra_passada) VALUES (%s, %s, %s)'
        # Define os valores a serem inseridos
        valores = (registro.nome, registro.telefone, registro.compra_passada)
        # Executa a instrução SQL
        self.cursor.execute(sql, valores)
        # Confirma a inserção no banco de dados
        self.conexao.commit()
        print('Registro adicionado.')

    # Método para listar os registros
    def listar_registro(self):
        # Executa a consulta SQL para selecionar os registros
        self.cursor.execute('SELECT nome, telefone, compra_passada FROM registro')
        # Recupera todas as linhas de resultado
        registros = self.cursor.fetchall()
        # Itera sobre os registros e imprime os valores
        for registro in registros:
            print(f'Nome: {registro[0]}, Telefone: {registro[1]}, Compra Passada: {registro[2]}')

    # Método para fechar a conexão com o banco de dados
    def fechar_conexao(self):
        # Fecha o objeto cursor
        self.cursor.close()
        # Fecha a conexão com o banco de dados
        self.conexao.close()

# Cria uma instância da classe SistemaCRM
sistema = SistemaCRM()
# Solicita ao usuário informações do registro
nome = input('Seu nome: ')
telefone = input('Número de telefone: ')
compra_passada = input('Qual foi a sua compra passada? ')
# Cria um objeto Registro com as informações fornecidas
registro = Registro(nome, telefone, compra_passada)
# Adiciona o registro ao sistema CRM
sistema.adicionar_registro(registro)

print('Registros salvos:')
# Lista os registros do sistema CRM
sistema.listar_registro()

# Fecha a conexão com o banco de dados
sistema.fechar_conexao()
