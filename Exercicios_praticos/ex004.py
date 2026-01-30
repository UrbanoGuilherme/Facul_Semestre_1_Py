#Peça 5 nomes ao usuário, armazene em uma lista e mostre:

nomes = []

for i in range(5):
      nome = str(input("digite um nome: "))
      nomes.append(nome)
print("Os nomes digitados foram: {}".format(nomes))
