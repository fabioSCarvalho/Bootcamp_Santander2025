class Bicicletas:
    def __init__(self, cor, modelo, ano, valor ):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("plim plim...")
    
    def parar(self):
        print("parando bicileta")
        print("bicicleta parada")
    
    def correr(self):
        print("vruummm")

   # def __str__(self):
   #     return f"Bicileta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
b1 = Bicicletas("vermelha", "calor", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor,b1.modelo,b1.ano,b1.valor)
b2 = Bicicletas("verde", "monark", 2000, 189)
print(b2)