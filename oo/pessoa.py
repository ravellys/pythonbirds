class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=25):
       self.idade = idade
       self.nome = nome
       self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá! eu sou o {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe( cls ):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho)
    del luciano.filhos
    luciano.sobrenome = 'Ramalho'
    luciano.olhos = 1
    del luciano.olhos
    Pessoa.olhos = 3
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(luciano.olhos)
    print(id(luciano.olhos),
          id(Pessoa.olhos),
          id(renzo.olhos)
          )
    print(Pessoa.metodo_estatico(),
          luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),
          luciano.nome_e_atributos_de_classe())
