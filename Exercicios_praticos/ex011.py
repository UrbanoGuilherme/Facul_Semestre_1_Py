#Peça um número ao usuário e trate o erro caso ele digite algo que não seja um número.

while True:
    try:
        n = float(input("Digite um número:"))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número válido.")
        
