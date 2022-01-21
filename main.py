from kivymd.app import MDApp 
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from view.tela_cadastro.telacadastroexercicio import TelaCadastroExercicio
from view.tela_lista_exercicios.telalistaexercicios import TelaListaExercicios
from view.tela_email.telaemail import TelaEmail
class Gerenciador(ScreenManager):
    pass

class Main(MDApp):
    Window.size = (350, 600)

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        return Gerenciador()

if __name__ == "__main__":
    app = Main()
    app.run()