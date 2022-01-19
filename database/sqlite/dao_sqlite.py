import sqlite3

class SqliteDatabase:
    def __init__(self):
        self.con = sqlite3.connect('patine.db')
        self.cursor = self.con.cursor()
        self.criarTabela()

    def criarTabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS exercicios(id integer PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255) NOT NULL, descricao VARCHAR(255) NOT NULL, url_imagem VARCHAR(255))")
        self.con.commit()

    def listar(self):
        sql = "SELECT * FROM exercicios"
        exercicios = self.cursor.execute(sql).fetchall()

        return exercicios        

    def listarUm(self, id):
        sql = "SELECT * FROM exercicios WHERE id = ?"
        exercicio = self.cursor.execute(sql, (id,)).fetchall()
        return exercicio    

    def salvarExercicio(self, ex):
        if ex.id is None:
            sql = "INSERT INTO exercicios(nome, descricao, url_imagem) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (ex.nome, ex.descricao, ex.urlImagem))
        else:
            sql = "UPDATE exercicios SET nome = ?, descricao = ?, url_imagem = ? WHERE id = ?"
            self.cursor.execute(sql, (ex.nome, ex.descricao, ex.urlImagem, ex.id,))

        self.con.commit()

    def excluir(self, id):
        sql = "DELETE FROM exercicios WHERE id = ?"
        self.cursor.execute(sql, (id,))
        self.con.commit()

    def close_db_connection(self):
        self.con.close()