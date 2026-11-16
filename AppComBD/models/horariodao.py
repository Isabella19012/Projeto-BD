import pyodbc
from .horario import Horario


class HorarioDAO:
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
                INSERT INTO Horario (data, confirmado, id_cliente, id_servico)
                VALUES (?, ?, ?, ?)
            """
            cls.execute(sql,(obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_servico()),)
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        try:
            cls.abrir()
            sql = "SELECT id, nome, email, fone, senha FROM Horario"
            cursor = cls.execute(sql)
            rows = cursor.fetchall()
            return [Horario(*row) for row in rows]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        try:
            cls.abrir()
            sql = "SELECT id, data, confirmado, id_cliente, id_servico FROM Horario WHERE id = ?"
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return Horario(*row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        try:
            cls.abrir()
            sql = """
                UPDATE Horario SET data=?, confirmado=?, id_cliente=?, id_servico=?
                WHERE id=?
            """
            cls.execute(sql,(obj.get_data(),obj.get_confirmado(),obj.get_id_cliente(),obj.get_id_servico(),obj.get_id(),),)
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, id):
        try:
            cls.abrir()
            sql = "DELETE FROM Horario WHERE id=?"
            cls.execute(sql, (id,))
        finally:
            cls.fechar()

if __name__ == "__main__":
    try:
        HorarioDAO.abrir()
        print("Conexão bem-sucedida!")
        HorarioDAO.fechar()
    except Exception as err:
        print(f"Erro BD: {err}")