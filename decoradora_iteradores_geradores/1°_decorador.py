def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar')
        funcao()
        print('Faz algo depois de executar')
    return envelope

def ola_mundo():
    print("olá, mundo")

ola_mundo_teste = meu_decorador(ola_mundo)
ola_mundo_teste()