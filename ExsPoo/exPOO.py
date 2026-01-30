class Teste:
    """"
essa classe cria um teste com nome e idade
    """
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos."
    
g1 = Teste(nome= "Maria", idade=30)
g1.aniversario()
print(g1)


g2 = Teste(nome="Gui", idade=25)
g2.aniversario()
print(g2)

print(g1.__doc__)

print("OI")
