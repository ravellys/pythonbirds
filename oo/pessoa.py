class Pessoa:
    def __init__(self, *filhos, nome=None, idade=25):
       self.idade = idade
       self.nome = nome
       self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá! eu sou o {self.nome}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa('renzo', nome = 'Luciano')
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho)