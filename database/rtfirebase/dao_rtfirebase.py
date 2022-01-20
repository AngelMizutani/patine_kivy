import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('database/rtfirebase/credenciais/fir-992d3-firebase-adminsdk-ig3wk-7bce28c352.json')
default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://fir-992d3.firebaseio.com/'
            })
ref = db.reference("/exercicios")

class RTFirebase:

    def listar(self):
        exercicios_lista = []
        exercicios = ref.get()
        for key, value in exercicios.items():
            exercicio = [key, value["nome"], value["descricao"], value["url_imagem"]]
            
            exercicios_lista.append(exercicio)
        return exercicios_lista

    def listarUm(self, id):
        exercicios = ref.get()
        exercicios_lista = []
        for key, value in exercicios.items():
            if (key == id):
                exercicio = [key, value["nome"], value["descricao"], value["url_imagem"]]
                exercicios_lista.append(exercicio)

        return exercicios_lista 

    def salvarExercicio(self, ex):
        ex_json = {
            "nome": ex.nome,
            "descricao": ex.descricao,
            "url_imagem": ex.urlImagem
        }
        if (ex.id is None):
            ref.push(ex_json)
        else:
            key = ex.id
            ref.child(key).update(ex_json)

    def excluir(self, id):
        exercicios = ref.get()
        for key, value in exercicios.items():
            if (key == id):
                ref.child(key).set({})