#Criação de um sistema bancário 

import re


print("Bem-vindo ao Sistema Bancário!\n")
print("Para iniciar, por favor digite seu numero de cpf: \n")
cpf = input("CPF: ")
cpf = re.sub(r"\D", "", cpf)
if len(cpf) != 11:
        print("CPF inválido. Por favor, insira um CPF válido com 11 dígitos.\n")
        exit()
        


print("Bem-vindo, usuário {}!\n".format(cpf))

saldo = 0

while True:
    print("Selecione a opção desejada: \n")
    print("1 - Depositar\n")
    print("2 - Fazer pix\n")
    print("3 - Sacar\n")
    print("4 - Verificar saldo\n")
    print("5 - Sair\n")
    opcao = int(input("Opção: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        saldo += valor_deposito
        print("Depósito de R${:.2f} realizado com sucesso".format(valor_deposito))
        print("Seu saldo atual é de R${:.2f}\n".format(saldo))

    elif opcao == 2:
        valor_pix = float(input("Digite o valor do pix: R$ \n"))
        if valor_pix > saldo: 
            print("Saldo insuficiente para realizar o pix.\n")
            continue

        while True:
            print("Selecione o tipo de chave pix: \n")
            print("1 - CPF\n")
            print("2 - E-mail\n")
            print("3 - Telefone\n")
            print("4 - Aleatória\n")
            print("5 - Voltar\n")
            tipo_chave = int(input("Opção: "))

            if tipo_chave in [1, 2, 3, 4]:
                chave_pix = input("Digite a chave pix: \n")
                if valor_pix <= saldo:
                    saldo -= valor_pix
                    print("Pix de R${:.2f} realizado com sucesso para a chave {}.\n".format(valor_pix, chave_pix))
                    print("Seu saldo atual é de R${:.2f}\n".format(saldo))
                else:
                    print("Saldo insuficiente para realizar o pix.\n")
                       
            elif tipo_chave == 5:
                break

    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado: R$ \n"))
        if valor_saque <= saldo:
            saldo -= valor_saque
            print("Saque de R${:.2f} realizado com sucesso.\n".format(valor_saque))
            print("Seu saldo atual é de R${:.2f}\n".format(saldo))
        else: 
            print("Saldo insuficiente para realizar o saque.\n")
            
    elif opcao == 4: 
        print("Seu saldo atual é de R${:.2f}\n".format(saldo))

    elif opcao == 5:
        print("Obrigado por utilizar nosso sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.\n")
         