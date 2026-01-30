#Crie uma função que receba um número inteiro como parâmetro e retorne se ele é par ou ímpar.

def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
num = int(input("Digite um número inteiro: "))
resultado = par_impar(num)
print("O número {} é {}.".format(num, resultado))


