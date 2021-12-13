import os


from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    Window.size = (400, 600)

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "view/screenmanager.kv"),
        os.path.join(os.getcwd(), "view/telaExercicio.kv"),
        os.path.join(os.getcwd(), "view/telaCadastro.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "view.screenmanager",
        "TelaExercicio": "view.telaExercicio",
        "TelaCadastro": "view.telaCadastro"
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self, **kwargs):
        self.theme_cls.primary_palette = "Purple"
        return Factory.MainScreenManager()


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()