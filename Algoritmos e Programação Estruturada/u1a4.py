#Com o intuito de manter a progressão do treinamento e contribuir com o avanço tanto teórico quanto prático, proponha à sua equipe de estagiários o desenvolvimento de um programa em C que calcule a média da quantidade de produtos vendidos anualmente por uma empresa de varejo com base nos dados apresentados na Tabela 1. Qual é a média de produtos vendidos em 2020, 2021 e 2022? É possível identificar qual ano teve a média mais alta? Há alguma outra abordagem para comparar os dados? Certifique-se de apresentar o programa resultante para toda a equipe.



dados = {}

while True:
    print("Selecione a opção desejada: \n")
    print("1 - inserir dados de um ano\n")
    print("2 - calcular a média anual de produtos vendidos de um ano especifico\n")
    print("3 - calcular a média anual de produtos vendidos de todos os anos\n")
    print("4 - sair\n")

    opcao = int(input("Opção: "))

    if opcao == 1:
        ano = int(input("Digite o ano a ser analisado: "))
        celulares = int(input("\n Quantos celulares foram vendidos em {}: ".format(ano)))
        tablets = int(input("\nQuantos tablets foram vendidos em {}: ".format(ano)))
        notebooks = int(input("\nQuantos notebooks foram vendidos em {}: ".format(ano)))                                          
        total_vendas = celulares + tablets + notebooks

        dados[ano] = {
            "celulares": celulares,
            "tablets": tablets,
            "notebooks": notebooks,
            "total_vendas": total_vendas
        }
        print("\nDados do ano{} inseridos com sucesso!\n".format(ano))
    
    elif opcao == 2:
        ano  = int(input("Digite o ano a ser analisado: "))
        if ano in dados:
            media_anual = dados[ano]["total_vendas"]/3
            print("\n a média de vendas anual de {} é: {:.2f}\n".format(ano, media_anual))
        else:
            print("\nDados do ano {} não encontrados. Por favor, insira os dados primeiro.\n".format(ano))

    elif opcao == 3: 
        if len(dados) == 0:
            print("\nNenhum dado disponível. Por favor, insira os dados primeiro.\n")
        else:
            soma_total_vendas = 0

            for ano in dados:
                soma_total_vendas += dados[ano]["total_vendas"]

            media_geral = soma_total_vendas / len(dados)
            print("\nA média geral de vendas anuais é: {:.2f}\n".format(media_geral))
    
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.\n")
