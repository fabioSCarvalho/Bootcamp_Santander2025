from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        print("ligando a TV")

    @abstractmethod
    def desligar(self):
        print("desligando a TV...")
        print("desligado")

class ControleTV(Controle_remoto):
    def ligar(self):
        print("ligando a TV")

    def desligar(self):
        print("desligando a TV...")
        print("desligado")
controle = ControleTV()

controle.ligar()
controle.desligar()
