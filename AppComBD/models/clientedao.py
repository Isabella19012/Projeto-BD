from models.cliente import Cliente
import json
import pyodbc



try:

    string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'

    conexao = pyodbc.connect(string_conexao)
    print("Conexão bem-sucedida!")
    print()
    print('Tabela Cliente')

    class ClienteDAO:
        def __conexao(self):
                string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'
                return pyodbc.connect(string_conexao)


        def inserir(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "INSERT INTO Cliente (nome, email, fone) VALUES (?, ?, ?)"
            valores = (obj.get_nome(), obj.get_email(), obj.get_fone())
        
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()

        def listar(self):    
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "SELECT id, nome, email, fone FROM Cliente"
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            objeto_clientes = []
            
            for reg in registros:
                c = Cliente(reg[0], reg[1], reg[2], reg[3]) 
                objeto_clientes.append(c)
                
            cursor.close()
            conexao.close()
            return objeto_clientes

        def listar_id(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"SELECT id, nome, email, fone FROM Cliente WHERE id = {id}"
            cursor.execute(sql)
            
            reg = cursor.fetchone()
            cursor.close()
            conexao.close()
            
            if reg:
                return Cliente(reg[0], reg[1], reg[2], reg[3])
            return None
        def atualizar(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            # Usando ? nos parâmetros para evitar problemas com textos, aspas ou SQL Injection
            sql = "UPDATE Cliente SET nome = ?, email = ?, fone = ? WHERE id = ?"
            valores = (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_id())
            
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        def excluir(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"""
            delete from Cliente where id = {id}

            """
            cursor.execute(sql)
            cursor.close()
            conexao.close()


except Exception as err:
    print(f"Erro BD: {err}")