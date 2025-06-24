saldo = 0 
extrato = "" 
contador_depositos = 0 
contador_saques = 0
LIMITE_SAQUES = 500.00
QUANTIDADE_DE_SAQUES_DIARIOS = 3

menu = """
============================
     Banco DIO
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Sair
============================
"""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = int(input("Quanto deseja depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            contador_depositos = contador_depositos + 1
            extrato += f"deposito: R${deposito:.2f} \n"
        else:
            print("Não é possivel depositar valores menores que R$ 0,01(um centavo)")

    elif opcao == 2:
        saque = int(input('Quanto deseja sacar: '))
        if contador_saques < QUANTIDADE_DE_SAQUES_DIARIOS:
            if saque <= LIMITE_SAQUES:
                if saque <= saldo :
                    saldo = saldo - saque
                    print(f"Você sacou R${saque:.2f}")
                    contador_saques = contador_saques + 1
                    extrato += f"saque: R${saque:.2f} \n"
                else:
                    print("Não será possível sacar dinheiro por falta de saldo") 
            else:
                print(f"Valor limite excedido! Limite de saque de até R${LIMITE_SAQUES:.2f}")   
        else:
            print("limite de saque diario excedido")

    elif opcao == 3:
        print(f"""
=============================
     EXTRATO
Saldo: R${saldo:.2f}
---------------------
{extrato}
=============================
        """)
    
    elif opcao == 4 :
        break

    else:
        print("Operação inválida")

