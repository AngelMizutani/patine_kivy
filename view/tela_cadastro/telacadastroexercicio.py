from kivymd.uix.screen import MDScreen 
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

from entidades.exercicio import Exercicio
from service.exercicio_service import ExercicioService

Builder.load_file("view/tela_cadastro/telacadastroexercicio.kv")

service = ExercicioService()

class TelaCadastroExercicio(MDScreen):
    nome_exercicio = ObjectProperty(None)
    descricao_exercicio = ObjectProperty(None)
    url_imagem_exercicio = ObjectProperty(None)

    def __init__(self, ex_id=None, **kw):
        super().__init__(**kw)
        self.ex_id = ex_id
        print(ex_id)

    def build(self):
        return TelaCadastroExercicio()

    def irParaLista(self):
        self.parent.current = 'lista'

    def salvar(self):
        label = self.ids.texto_erro
        
        if (self.nome_exercicio.text == ''):
            label.text = 'O nome é obrigatório'
        
        elif (self.descricao_exercicio.text == ''):
            label.text = 'A descrição é obrigatória!'

        else:
            ex = Exercicio(
                None,
                self.nome_exercicio.text,
                self.descricao_exercicio.text,
                self.url_imagem_exercicio.text
            )
            service.salvar(ex)

            label.text = ''
            self.nome_exercicio.text = ''
            self.descricao_exercicio.text = ''
            self.url_imagem_exercicio.text = ''
            self.irParaLista()
