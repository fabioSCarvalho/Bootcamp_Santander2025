'''
     Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:

Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
Não pode começar ou terminar com "@".
Não pode conter espaços.
Entrada
    Uma string contendo o e-mail a ser validado.
Saída
    "E-mail válido" se o e-mail estiver no formato correto.
    "E-mail inválido" caso contrário.'''

# Entrada do usuário
email = input("Informe o Email:").strip()

if "@" in email:
    index = email.index("@")
    if index != 0 and (email[index+1:] == "gmail.com" or email[index+1:] == "outlook.com"):
            print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")
