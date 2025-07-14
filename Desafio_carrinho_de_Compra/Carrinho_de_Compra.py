'''
    Descrição
Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra.
'''

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input("Informe a quantidade de itens que tesrá na lista: ").strip())

# Loop para adicionar itens ao carrinho
for item in range(n):
    linha = input(f"Informe o  {item +1 }° item e o valor: ex: 'Pão 3.50' : ").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra
for item, valor in carrinho:
    print(f"{item}:R${valor:.2f}")
print("Total: R${total:.2f}")