'''
escrição
Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

📌 Regras de desconto:

"DESCONTO10": 10% de desconto.
"DESCONTO20": 20% de desconto.
"SEM_DESCONTO": Sem desconto.
Entrada
    Preço original do produto.
    Código do cupom digitado.
Saída
    Preço final após aplicar o desconto. Com duas casas decimais.
'''

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Informe o valor do produto: ").strip())
cupom = input("Informe o cupom de desconto:").strip().upper()

# TODO: Aplique o desconto se o cupom for válido:

if cupom in descontos.keys():
  desconto = preco - (preco * descontos[cupom])
  print(f"{desconto:.2f}")
else:
  print('Cupom de desconto inválido, você não teve desconto')