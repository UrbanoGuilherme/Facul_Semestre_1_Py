#Crie um dicionário com nome, idade e curso e imprima uma frase usando esses dados

pessoa = {}

qtd_infos = int(input("Quantos dados voce quer inserir no cadastro:"))
for i in range(qtd_infos):
    dado = str(input("Digite o nome da classe do dado:"))
    valor = str(input("Digite o valor dso dado: "))
    pessoa[dado] = valor

print("Os dados inseridos foram:")
for dado, valor in pessoa.items():
    print(f"{dado}:{valor}")
    