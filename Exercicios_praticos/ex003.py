# Peça números ao usuário até que ele digite 0.
# Ao final, mostre a soma de todos os números digitados.

dados = []

while True:
    num = int(input("Digite um numero inteiro (ou 0 para encerrar): "))
    if num != 0:
        dados.append(num)
    else:
        soma = sum(dados)
        print(dados)
        print("A soma dos valores é: {}".format(soma))
        break
   