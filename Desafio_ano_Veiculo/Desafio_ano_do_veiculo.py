'''Descrição
Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

Entrada
Marca, modelo e ano do veículo.
Saída
"Veículo antigo" se o carro tiver mais de 20 anos.
"Veículo novo" caso contrário.'''


from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
    def __init__(self, marca, modelo, ano_veiculo):
        self.marca = marca
        self.modelo = modelo
        self.ano_veiculo = int(ano_veiculo)
    

    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:    
    def verificar_antiguidade(self):
      ano_atual =  datetime.now().year
      idade = ano_atual - self.ano_veiculo  

      if idade > 20:
        return "Veículo antigo"
      else:
        return "Veículo novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())