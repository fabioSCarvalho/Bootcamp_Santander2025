'''Descrição
Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.

Entrada
Lista de itens e seus respectivos preços.
Saída
O valor total da conta.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2
Pizza 40.00
Suco 7.50	47.50'''

class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self,preco):
        # TODO: Adicione o preço do item à lista:
        preco = float(preco)
        self.itens.append(preco)
        
        
    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    def calcular_total(self):
        # TODO: Retorne a soma de todos os preços
        total = sum(self.itens)
        return f"{total:.2f}"

quantidade_pedidos = int(input('Infomre a quantidade de pedidos que irá fazer ?: ').strip())

pedido = Pedido()


for n in range(quantidade_pedidos):
    entrada = input(f"Informe o  {n +1 }° item e o valor: ex: 'Pão 3.50' :").strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(preco)
# TODO: Exiba o total formatado com duas casas decimais:
print(pedido.calcular_total())