<<<<<<< HEAD
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
=======
from models.horario import Horario
import pyodbc


try:

    string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'

    conexao = pyodbc.connect(string_conexao)
    print("Conexão bem-sucedida!")
    print()
    print('Tabela Horário')

    class ServicoDAO:
        def __conexao(self):
                string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=isabella_pratica;UID=sa;PWD=senha@12345'
                return pyodbc.connect(string_conexao)


        def inserir(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "INSERT INTO Horario (data, confirmado, id_servico, id_cliente) VALUES (?, ?, ?, ?)"
            valores = (obj.get_data(), obj.get_confirmado(), obj.get_servico(), obj.get_cliente())
        
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()

        def listar(self):    
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "SELECT id, data, confirmado, id_servico, id_cliente FROM Horario"
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            objeto_horarios = []
            
            for reg in registros:
                c = Horario(reg[0], reg[1], reg[2], reg[3], reg[4]) 
                objeto_horarios.append(c)
                
            cursor.close()
            conexao.close()
            return objeto_horarios

        def listar_id(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"SELECT id, data, confirmado, id_servico, id_cliente FROM Horario WHERE id = {id}"
            cursor.execute(sql)
            
            reg = cursor.fetchone()
            cursor.close()
            conexao.close()
            
            if reg:
                return Horario(reg[0], reg[1], reg[2], reg[3], reg[4])
            return None
        def atualizar(self, obj):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = "UPDATE Horario SET data = ?, data = ?, id_servico = ?, id_cliente = ? WHERE id = ?"
            valores = (obj.get_data(), obj.get_data(), obj.get_id_servico(), obj.get_id_cliente())
            
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
        def excluir(self, id):
            conexao = self.__conexao()
            cursor = conexao.cursor()
            sql = f"""
            delete from Horario where id = {id}

            """
            cursor.execute(sql)
            cursor.close()
            conexao.close()


except Exception as err:
    print(f"Erro BD: {err}")
>>>>>>> 54d8a0abc51d3f67c191a58b9aae8a291d19d125
