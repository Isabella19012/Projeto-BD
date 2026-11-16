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