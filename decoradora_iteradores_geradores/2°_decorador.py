def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar')
        funcao()
        print('Faz algo depois de executar')
    return envelope

@meu_decorador
def ola_mundo():
    print("olá, mundo")

    
ola_mundo()



'''ola_mundo = meu_decorador(ola_mundo)'''


''' 
------------------------------------------------
colocar o @decorador na função e chamar ela diremente é a mesma coisa de eu fazer

def ola_mundo_funcao():
    print("olá, mundo")

ola_mundo_funcao = meu_decorador(ola_mundo
------------------------------------------------
                              '''