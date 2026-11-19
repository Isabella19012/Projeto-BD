<<<<<<< HEAD
import pyodbc
from .cliente import Cliente


class ClienteDAO:
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
                INSERT INTO Cliente (nome, email, fone)
                VALUES (?, ?, ?, ?)
            """
            cls.execute(sql,(obj.get_nome(), obj.get_email(), obj.get_fone()),)
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        try:
            cls.abrir()
            sql = "SELECT id, nome, email, fone FROM Cliente"
            cursor = cls.execute(sql)
            rows = cursor.fetchall()
            return [Cliente(*row) for row in rows]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        try:
            cls.abrir()
            sql = "SELECT id, nome, email, fone FROM Cliente WHERE id = ?"
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return Cliente(*row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        try:
            cls.abrir()
            sql = """
                UPDATE Cliente SET nome=?, email=?, fone=?
                WHERE id=?
            """
            cls.execute(sql,(obj.get_nome(),obj.get_email(),obj.get_fone(),obj.get_id(),),)
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, id):
        try:
            cls.abrir()
            sql = "DELETE FROM Cliente WHERE id=?"
            cls.execute(sql, (id,))
        finally:
            cls.fechar()

if __name__ == "__main__":
    try:
        ClienteDAO.abrir()
        print("Conexão bem-sucedida!")
        ClienteDAO.fechar()
    except Exception as err:
        print(f"Erro BD: {err}")
=======
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
>>>>>>> 54d8a0abc51d3f67c191a58b9aae8a291d19d125
