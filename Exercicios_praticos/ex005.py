#Dada uma lista de números, mostre o maior e o menor valor.

list_nums = []


num = int(input("Quantos números voce quer inserir na lista? "))

for i in range(num):
    n = float(input("Digite um número: "))
    list_nums.append(n)

print("A lista de número é: {}\n".format(list_nums))
print("O maior número da lista é: {}\n".format(max(list_nums)))
print("O menor número da lista é: {}\n".format(min(list_nums)))


