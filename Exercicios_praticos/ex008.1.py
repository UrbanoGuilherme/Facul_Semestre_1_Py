# Calculadora

def soma(a,b):
    return a+b

def subtração(a,b):
    return a-b

def multiplicação(a,b):
    return a*b

def divisão(a,b):
    return a/b

while True:
    print("Escolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    operação = input("Digite o número da operação desejada: ")
    
    if operação == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", soma(a, b))
    elif operação == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", subtração(a, b))
    elif operação == "3":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", multiplicação(a, b))
    elif operação == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if b == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue
        print("Resultado:", divisão(a, b))
    elif operação == "5":
        print("Saindo da calculadora. Até mais!")
        break
    else:
        print("Operação inválida. Tente novamente.")