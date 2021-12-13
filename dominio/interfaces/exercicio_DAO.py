from abc import ABC, abstractmethod
import sqlite3

from dominio.entidades.exercicioEntidade import ExercicioEntidade

class ExercicioDAO(ABC):
    
    @abstractmethod
    def salvar(self, ExercicioEntidade):
        pass

    @abstractmethod
    def deletar(self, id):
        pass

    @abstractmethod
    def listar(self, ExercicioEntidade):
        pass