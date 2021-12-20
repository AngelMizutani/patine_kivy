from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from database.dao.exercicio_dao_impl import ExercicioDaoImpl as dao

class TelaCadastro(MDScreen):
    def irParaLista(self):
        print('clicou')
        MDApp.get_running_app().root.current = 'lista'

    def salvarExercicio(self):
        dao.salvar()