#Peça uma frase ao usuário e informe quantas palavras ela possui.

frase = str(input("Digite uma frase:"))
palavras = frase.split()
num_palavras = len(palavras)

print("A frase digitada possui {} palavras.".format(num_palavras))
