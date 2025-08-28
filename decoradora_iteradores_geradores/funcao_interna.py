def principal():
    print("executantado a função principal")

    def funcao_interna():
        print('executando a função interna')

    def funcao_2():
        print("executando a duncao 2")

    
    funcao_interna()
    funcao_2()

principal()