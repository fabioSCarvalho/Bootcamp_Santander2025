LIMITE_SAQUES = 3
AGENCIA = '0001'

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios= []
contas = []

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    print(menu)

def filtrar_usuarios(cpf, lista_de_usuarios):
     usuario_filtrado = ''
     for usuario in lista_de_usuarios:
          if usuario["cpf"] == cpf:
               usuario_filtrado = usuario
     return usuario_filtrado if usuario_filtrado else None
    
def criar_usuario(cpf):
     usuarios_filtrado = filtrar_usuarios(cpf, usuarios)
     if usuarios_filtrado:
          print('cpf já cadastrado')
          return
     nome = input('Informe o nome completo: ').strip()
     nascimento = input('informe data de nascimento (dd-mm-aaa): ').strip()
     endereco =input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ').strip()
     usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereco": endereco})

def saque(*, saldo,valor,extrato,numero_saques, limite,limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def mostrar_extrato(saldo,/,*,extrato):
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_conta(agencia, numero_conta, cpf):
    usuarios_filtrado = filtrar_usuarios(cpf, usuarios)
    if usuarios_filtrado:
        print( "\n=== Conta criada com sucesso! ===")
        return{'agencia': agencia, 'numero_conta': numero_conta,'cpf': cpf}
    print('usuario não encontrado')

         
def listar_contas(contas):
    if not contas:
        print("\n=== Nenhuma conta cadastrada. ===")
        return
    for conta in contas: 
        linha = f'''
        Agencia: {conta['agencia']} \n
        Conta: {conta['numero_conta']}\n
        Cpf: {conta['usuarios']}
        '''
        print(linha)

while True:
    menu()
    opcao = input('informe a opção desejada: ').strip().upper()

    if opcao == 'S':
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo,extrato=extrato,valor=valor_saque,numero_saques=numero_saques, limite=limite, limite_saques=LIMITE_SAQUES)
    
    elif opcao =='D':
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 'E':
        mostrar_extrato(saldo,extrato=extrato)
    
    elif opcao == 'NC':
         numero_conta = len(contas) + 1
         cpf = input('informe o cpf do usuario (apenas os numero): ').strip()
         nova_conta = criar_conta(AGENCIA,numero_conta,cpf)
         if nova_conta:
            contas.append(nova_conta)

    elif opcao == 'NU':
        cpf = input('informe o cpf parar criar usuario (apenas os numero): ').strip()
        criar_usuario(cpf)

    elif opcao == 'LC':
        listar_contas(contas)
 
    elif opcao == "Q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print(contas)