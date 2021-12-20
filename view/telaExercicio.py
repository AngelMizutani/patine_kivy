from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from database.dao.exercicio_dao_impl import ExercicioDaoImpl as dao

class TelaExercicio(MDScreen):
    
    def irParaCadastro(self):
        print('clicou')
        MDApp.get_running_app().root.current = 'cadastro'

    def listarExercicios(self):
        exercicios = dao.listar()
        for exercicio in exercicios:
            exercicios.append(exercicio)