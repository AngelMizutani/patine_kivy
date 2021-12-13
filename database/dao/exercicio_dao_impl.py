import sqlite3
from dominio.interfaces.exercicio_DAO import ExercicioDAO


class exercicioDaoImpl(ExercicioDAO):
    def __init__(self):
        self.conexao = sqlite3.connect("patine_kivy")
        self.cursor = self.conexao.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , nome TEXT (255) NOT NULL
            , descricao TEXT (255) NOT NULL)'''
        self.cursor.execute(sql)
        
    def salvar(self, ExercicioEntidade):
        self.conexao.sqlite3.connect("patine_kivy")
        self.cursor = self.conexao.cursor()
        if (ExercicioEntidade.id.isnull):
            sql = 'INSERT INTO exercicios (nome, descricao) VALUES (?, ?)'
            self.cursor.execute(sql, [ExercicioEntidade.nome, ExercicioEntidade.descricao])
            self.conexao.commit()

        else:
            sql = 'UPDATE exercicios SET (nome, descricao) = (?, ?) WHERE id = ?'
            self.cursor.execute(sql, [ExercicioEntidade.nome, ExercicioEntidade.descricao, ExercicioEntidade.id])
            self.conexao.commit()  

    def deletar(self, id):
        self.conexao.sqlite3.connect("patine_kivy")
        self.cursor = self.conexao.cursor()
        sql = 'DELETE FROM exercicios WHERE id = ?'
        self.cursor.execute(sql, [id])
        self.conexao.commit()

    def listar(self, ExercicioEntidade):
        self.conexao.sqlite3.connect("patine_kivy")
        self.cursor = self.conexao.cursor()
        sql = 'SELECT * FROM exercicios'
        self.cursor.execute(sql)
        exercicios = self.cursor.fetchall()
        for exercicio in exercicios:
            ExercicioEntidade.id = exercicio[0]
            ExercicioEntidade.nome = exercicio[1]
            ExercicioEntidade.descricao = exercicio[2]