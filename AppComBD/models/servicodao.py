<<<<<<< HEAD
import pyodbc
from .servico import Servico


class ServicoDAO:
    conn = None
    string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_atv;UID=sa;PWD=senha@12345'

    @classmethod
    def abrir(cls):
        cls.conn = pyodbc.connect(cls.string_conexao)

    @classmethod
    def fechar(cls):
        if cls.conn:
            cls.conn.close()
            cls.conn = None

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or ())
        cls.conn.commit()
        return cursor

    @classmethod
    def inserir(cls, obj):
        try:
            cls.abrir()
            sql = """
                INSERT INTO Servico (nome, email, fone, senha)
                VALUES (?, ?, ?, ?)
            """
            cls.execute(sql,(obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()),)
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        try:
            cls.abrir()
            sql = "SELECT id, nome, email, fone, senha FROM Servico"
            cursor = cls.execute(sql)
            rows = cursor.fetchall()
            return [Servico(*row) for row in rows]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        try:
            cls.abrir()
            sql = "SELECT id, descricao, valor FROM Servico WHERE id = ?"
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return Servico(*row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj): 
        try:
            cls.abrir()
            sql = """
                UPDATE Servico SET descricao=?, valor=?
                WHERE id=?
            """
            cls.execute(sql,(obj.get_nome(),obj.get_email(),obj.get_fone(),obj.get_senha(),obj.get_id(),),)
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, id):
        try:
            cls.abrir()
            sql = "DELETE FROM Servico WHERE id=?"
            cls.execute(sql, (id,))
        finally:
            cls.fechar()

if __name__ == "__main__":
    try:
        ServicoDAO.abrir()
        print("Conexão bem-sucedida!")
        ServicoDAO.fechar()
    except Exception as err:
        print(f"Erro BD: {err}")
=======
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
>>>>>>> 54d8a0abc51d3f67c191a58b9aae8a291d19d125
