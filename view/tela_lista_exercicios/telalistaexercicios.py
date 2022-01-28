from kivymd.uix.screen import MDScreen 
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget, IRightBodyTouch
from kivymd.uix.dialog import MDDialog 
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

from entidades.exercicio import Exercicio
from service.exercicio_service import ExercicioService

Builder.load_file("view/tela_lista_exercicios/telalistaexercicios.kv")

exercicios = [
    {
        'nome':'freio em T', 
        'descricao':'faça um T com os patins para diminuir a velocidade ou parar',
        'urlImagem': 'https://i.ytimg.com/vi/DeAZogIb464/maxresdefault.jpg'},
    {
         'nome': 'limões',
         'descricao': 'desenhe limões com os patins',
         'urlImagem': 'https://i.ytimg.com/vi/H1CPIlWfrJU/maxresdefault.jpg'},

    {
        'nome':'freio em cunha', 
        'descricao':'faça um V invertido para diminuir a velocidade',
        'urlImagem': 'https://i.ytimg.com/vi/JLS56y636IY/mqdefault.jpg'},
    {
         'nome': 'freio em cunha com passos',
         'descricao': 'vá aproximando as pontas dos patins gradativamente para parar',
         'urlImagem': 'https://i.ytimg.com/vi/XyKnryt-j8Q/maxresdefault.jpg'},
    {
         'nome': 'Freio de calcanhar',
         'descricao': 'use o freio do patins para parar',
         'urlImagem': 'https://i.ytimg.com/vi/-WJ97gUZ0fI/maxresdefault.jpg'}
]

service = ExercicioService()

class TelaListaExercicios(MDScreen):
    
    def __init__(self, **kw):
        super(TelaListaExercicios, self).__init__(**kw)
        self._on_enter_trig = trig = Clock.create_trigger(self._my_on_enter)
        self.bind(on_enter=trig)

    def _my_on_enter(self, *largs):
        self.listarExercicios()

    def irParaEmail(self):
        self.parent.current = 'email'
        self.limpar()

    def irParaCadastro(self):
        self.parent.current = 'cadastro'
        self.limpar()

    def addExercicio(self):
        for exercicio in exercicios:
            ex = Exercicio(None, exercicio['nome'], exercicio['descricao'], exercicio['urlImagem'])
            service.salvar(ex)
        self.limpar()
        self.listarExercicios()

    def listarExercicios(self):
        try:
            exercicios = service.listar()
            for exercicio in exercicios:
                ex = Exercicio(
                    exercicio[0],
                    exercicio[1], 
                    exercicio[2], 
                    exercicio[3]
                )
                exercicio_item = ExercicioItem(
                    ex_id = ex.id,
                    text = ex.nome,
                    secondary_text = ex.descricao
                )
                url_imagem = ''
                if (ex.urlImagem == ''):
                    url_imagem = 'view\images\patins.png'
                else:
                    url_imagem = ex.urlImagem
                exercicio_item.add_widget(ImageLeftWidget(source = url_imagem))
                self.ids.container.add_widget(exercicio_item)

        except Exception as e:
            print(e)
            pass

    def limpar(self):
        self.ids.container.clear_widgets()

    def recarregar(self):
        self.limpar()
        self.listarExercicios()

    def build(self):
        return TelaListaExercicios()

class ExercicioItem(TwoLineAvatarIconListItem):
    dialog = None
    dialogExcluir = None
    dialogEditar = None

    def __init__(self, ex_id=None, **kwargs):
        super().__init__(**kwargs)
        self.ex_id = ex_id

    def verDetalhe(self, item, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title = item.text,
                text = item.secondary_text,
                buttons=[
                    MDFlatButton(
                        text="FECHAR",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = lambda x: self.fecharDialog()

                    ),
                ],
            )
        self.dialog.open()

    def fecharDialog(self, *args):
        self.dialog.dismiss(force = True)

    def excluirItem(self, item):
        self.parent.remove_widget(item)
        service.excluir(item.ex_id)
        self.fecharDialogExcluir()

    def abrirDialogExcluir(self, item):
        self.fecharDialog()
        if not self.dialogExcluir:
            self.dialogExcluir = MDDialog(
                title = 'Confirmar exclusão?',
                text = item.text,
                buttons=[
                    MDFlatButton(
                        text="EXCLUIR",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= lambda x: self.excluirItem(item)
                    ),
                    MDFlatButton(
                        text="CANCELAR",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = lambda x: self.fecharDialogExcluir()

                    ),
                ],
            )
        self.dialogExcluir.open()

    def fecharDialogExcluir(self, *args):
        self.dialogExcluir.dismiss(force = True)

    def abrirDialogEditar(self, item):
        if not self.dialogEditar:
            self.dialogEditar = MDDialog(
                title = 'Editar Exercício',
                type = 'custom',
                content_cls = DialogEditar(ex_id = item.ex_id),
                buttons=[
                    MDFlatButton(
                        text="FECHAR",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = lambda x: self.fecharDialogEditar()

                    ),
                ],
            )
            
        self.dialogEditar.open()

    def fecharDialogEditar(self, *args):
        self.dialogEditar.dismiss(force = True)

class ItemContainer(IRightBodyTouch, MDBoxLayout):
    adaptative_width = True

class DialogEditar(MDBoxLayout):
    edit_nome: ObjectProperty(None)
    edit_descricao: ObjectProperty(None)
    edit_imagem: ObjectProperty(None)

    def __init__(self, ex_id=None, **kwargs):
        super().__init__()
        self.ex_id = ex_id
        self.carregarCampos(self.ex_id)

    def carregarCampos(self, ex_id):
        exercicio = service.listarUm(ex_id)
        
        self.edit_nome.text = exercicio[0][1]
        self.edit_descricao.text = exercicio[0][2]
        if exercicio[0][3] is None:
            self.edit_imagem.text = ''
        else:
            self.edit_imagem.text = exercicio[0][3]

    def editarItem(self):
        label = self.ids.edit_texto_erro

        if (self.edit_nome.text == ''):
            label.text = 'O nome é obrigatório'
        
        elif (self.edit_descricao.text == ''):
            label.text = 'A descrição é obrigatória!'

        else:
            ex = Exercicio(
                self.ex_id,
                self.edit_nome.text,
                self.edit_descricao.text,
                self.edit_imagem.text
            )

            service.salvar(ex)

            label.text = ''
            self.edit_nome.text = ''
            self.edit_descricao.text = ''
            self.edit_imagem.text = ''


    