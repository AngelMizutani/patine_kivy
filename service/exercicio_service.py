from database.sqlite.dao_sqlite import SqliteDatabase
from database.rtfirebase.dao_rtfirebase import RTFirebase
from database.mysql.dao_mysql import MySqlDatabase

class ExercicioService():
    def __init__(self):
        # self.dao = SqliteDatabase()
        self.dao = RTFirebase()
        # self.dao = MySqlDatabase()

    def listar(self):
        return self.dao.listar()

    def listarUm(self, id):
        return self.dao.listarUm(id)

    def excluir(self, id):
        return self.dao.excluir(id)

    def salvar(self, ex):
        return self.dao.salvarExercicio(ex)