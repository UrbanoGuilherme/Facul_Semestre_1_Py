#Peça um número ao usuário e informe se ele é par ou ímpar.

num = int(input("digite um numero inteiro: "))
if num % 2 == 0:
    print("O numero {} é par".format(num))
else: 
    print("O numero {} é impar".format(num))
    print