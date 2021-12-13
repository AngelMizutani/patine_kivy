import sqlite3
class Conexao():
    def __init__(self):
        self.conexao = sqlite3.connect("patine_kivy")
        self.cursor = self.conexao.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , nome TEXT (255) NOT NULL
            , descricao TEXT (255) NOT NULL)'''
        self.cursor.execute(sql)
