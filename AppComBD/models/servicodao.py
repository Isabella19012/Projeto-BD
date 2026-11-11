from models.servico import Servico
import pyodbc

try:

    string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'

    conexao = pyodbc.connect(string_conexao)
    print("Conexão bem-sucedida!")
    print()
    print('Tabela Serviço')

    class ServicoDAO:
        def __conexao(self):
                string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'
                return pyodbc.connect(string_conexao)


        def inserir(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "INSERT INTO Servico (descricao, valor) VALUES (?, ?)"
            valores = (obj.get_descricao(), obj.get_valor())
        
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()

        def listar(self):    
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "SELECT id, descricao, valor FROM Servico"
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            objeto_servicos = []
            
            for reg in registros:
                c = Servico(reg[0], reg[1], reg[2]) 
                objeto_servicos.append(c)
                
            cursor.close()
            conexao.close()
            return objeto_servicos

        def listar_id(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"SELECT id, descricao, valor FROM Servico WHERE id = {id}"
            cursor.execute(sql)
            
            reg = cursor.fetchone()
            cursor.close()
            conexao.close()
            
            if reg:
                return Servico(reg[0], reg[1], reg[2])
            return None
        def atualizar(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "UPDATE Servico SET descricao = ?, valor = ? WHERE id = ?"
            valores = (obj.get_descricao(), obj.get_valor(), obj.get_id())
            
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        def excluir(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"""
            delete from Servico where id = {id}

            """
            cursor.execute(sql)
            cursor.close()
            conexao.close()


except Exception as err:
    print(f"Erro BD: {err}")