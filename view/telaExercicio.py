from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class TelaExercicio(MDScreen):
    
    def irParaCadastro(self):
        print('clicou')
        MDApp.get_running_app().root.current = 'cadastro'