#Crie uma função que receba uma lista de notas e retorne a média dessas notas.

notas = []

def calcular_media(notas):
    if len(notas)== 0:
        return 0
    return sum(notas)/len(notas)

while True:
    print("\n Digite abaixo as notas (ou 000 para encerrar e calcular a média):\n")
    n = float(input("Digite a nota: "))
    if n != 000:
        notas.append(n)
    elif n < 0 or n > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")    
    elif n == 000:
        media = calcular_media(notas)
        print("\nA média das notas é: {:.2f}".format(media))
        break



