def menasgem(nome):
    print('Executntando nome')
    return f'oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá, tudo bem com você {nome}? '

def executar(funcao,nome):
    print('executando executar')
    return funcao(nome)

print(executar(menasgem,'fábio'))
print(executar(mensagem_longa,"fábio"))