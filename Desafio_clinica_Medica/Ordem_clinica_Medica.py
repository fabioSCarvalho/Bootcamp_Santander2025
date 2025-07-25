'''
Descrição
Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

📌 Critérios de Prioridade:

Pacientes acima de 60 anos têm prioridade.
Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
Os demais pacientes são atendidos por ordem de chegada.
Entrada
Um número inteiro n, representando a quantidade de pacientes.
n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
nome: string representando o nome do paciente.
idade: número inteiro representando a idade do paciente.
status: string que pode ser "urgente" ou "normal".
Saída
A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...
'''

# Entrada do número de pacientes
n = int(input("informe a quantidade de paciente: ").strip())

# Lista para armazenar pacientes
pacientes = []
ordem_atendimento = []

# Loop para entrada de dados
for paciente in range(n):
    nome, idade, status = input("Informe os dados do paciente: 'nome, idade, status': ").strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordem_por_idade(lista):
   ordem_por_idade = sorted(lista,key=lambda x:x[1], reverse=True)
   return ordem_por_idade

def ordem(Lista_paciente):
  paciente_comum = []
  paciente_por_idade= []
  paciente_urgente = []
  
  for paciente in Lista_paciente:
    if paciente[2] ==  'urgente':
        paciente_urgente.append(paciente)
    elif paciente[1] > 60:
        paciente_por_idade.append(paciente)
    else:
        paciente_comum.append(paciente)
  return paciente_urgente, paciente_por_idade, paciente_comum


# TODO: Exiba a ordem de atendimento com título e vírgulas:
urgentes, prioridade_por_idade, comum  = ordem(pacientes)

ordem = ordem_por_idade(urgentes) + ordem_por_idade(prioridade_por_idade) + ordem_por_idade(comum)
for paciente in ordem:
  ordem_atendimento.append(paciente[0])
print(f"Ordem de Atendimento: " + ', '.join(ordem_atendimento))

