# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input('Informe a quantidade de participantes: ').strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for participantes in range(n):
  participante_tema = input("Informe o nome e o tema do 1°: 'ex: fabio, fotografia': ").strip()
  posicao_virgula = participante_tema.rfind(",")
  participante = participante_tema[:posicao_virgula]
  tema = participante_tema[posicao_virgula + 1:]
  if tema in eventos:
    eventos[tema].append(participante)
  else:
    eventos[tema] = [participante]
  
# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")