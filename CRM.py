import mysql.connector

class Registro:
    def ___init___(self,nome,telefone,compra_passada):
        self.nome=nome
        self.telefone=telefone
        self.compra_passada=compra_passada

class SistemaCRM:
    def ___init___(self):
        self.conexao=mysql.connector.connect(
            host='localhost',
            user='root',
            passoword='he182555@',
            database='CRM'
        )
        self.cursor=self.conexao.cursor()

    def adicionar_resgistro(self,registro):
        sql='INSERT INTO registro(nome,telefone,compra_passada) values (%s,%s,%s)'
        valores=(registro.nome,registro.telefone,registro.compra_passada)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        print('registro adicionado')

    def listar_registro(self):
        self.cursor.execute('SELECT nome,telefone,compra_passada FROM registro')
        registro=self.cursor.fetchall()
        for registro in registro:
            print(f'nome:{registro[0]} telefone:{registro[1]} data de compra passada:{registro[1]}')
        
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

sistema=SistemaCRM()
nome=input('seu nome')
telefone=input('numero de telefone')
compra_passada=input('qual foi a sua compra passada?')
registro=Registro(nome,telefone,compra_passada)
sistema.adicionar_resgistro(registro)

print('registros salvos:')
sistema.listar_registro()

sistema.fechar_conexao