def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar')
        funcao(*args, **kwargs)
        print('Faz algo depois de executar')
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"olá, mundo {nome}!")

    
ola_mundo('Fábio')


'''Ultilizando o *args, **kwargs o decorador fica genérico, não precisa ficar alterando caso adicione mais arugumento na função'''