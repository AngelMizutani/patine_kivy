import requests

api_url = "http://192.168.56.1:8080/exercicio"

class MySqlDatabase:

    def listar(self):
        exercicios_lista = []
        exercicios = requests.get(api_url).json()
        for exercicio in exercicios:
            ex = [exercicio["id"], exercicio["nome"], exercicio["descricao"], exercicio["urlImagem"]]
            exercicios_lista.append(ex)
        return exercicios_lista

    def listarUm(self, id):
        exercicios_lista = []
        exercicios = requests.get(api_url).json()
        for exercicio in exercicios:
            if (exercicio["id"] == id):
                ex = [exercicio["id"], exercicio["nome"], exercicio["descricao"], exercicio["urlImagem"]]
                exercicios_lista.append(ex)
        return exercicios_lista

    def salvarExercicio(self, ex):
        ex_json = {
            "id": ex.id,
            "nome": ex.nome,
            "descricao": ex.descricao,
            "urlImagem": ex.urlImagem
        }
        if (ex.id is None):
            requests.post(api_url, json=ex_json)
        else:
            requests.put(api_url, json=ex_json)

    def excluir(self, id):
        api_url = "http://192.168.56.1:8080/exercicio/{}".format(id)
        requests.delete(api_url)