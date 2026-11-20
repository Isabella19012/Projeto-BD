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
        return cursor

    @classmethod
    def inserir(cls, obj):
        try:
            cls.abrir()
            sql = """
                INSERT INTO Cliente (nome, email, fone)
                VALUES (?, ?, ?)
            """
            cls.execute(sql,(obj.get_nome(), obj.get_email(), obj.get_fone()),)
            cls.conn.commit()
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
            cls.conn.commit()
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, id):
        try:
            cls.abrir()
            sql = "DELETE FROM Cliente WHERE id=?"
            cls.execute(sql, (id,))
            cls.conn.commit()
        finally:
            cls.fechar()

if __name__ == "__main__":
    try:
        ClienteDAO.abrir()
        print("Conexão bem-sucedida!")
        ClienteDAO.fechar()
    except Exception as err:
        print(f"Erro BD: {err}")
