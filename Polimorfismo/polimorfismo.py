class Passaro:
    def voar(self):
        print("voando ...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não pode voar")

        
# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ...")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())