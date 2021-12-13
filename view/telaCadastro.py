from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class TelaCadastro(MDScreen):
    def irParaLista(self):
        print('clicou')
        MDApp.get_running_app().root.current = 'lista'