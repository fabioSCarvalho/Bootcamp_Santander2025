class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} -{self.matricula} - {self.escola}"

def motrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante("guilherme",1)
aluno_2 = Estudante("Giovana",2)
motrar_valores(aluno_1,aluno_2)

Estudante.escola = "python"
aluno_3 = Estudante("chappie",3)
motrar_valores(aluno_1,aluno_3)
