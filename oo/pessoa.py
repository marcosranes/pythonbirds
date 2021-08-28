class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=6):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    marina = Pessoa(nome='Marina')
    marcos = Pessoa(marina, nome='Marcos', idade=39)
    print(Pessoa.cumprimentar(marina))
    print(id(marina))
    print(marina.cumprimentar())
    print(marina.nome)
    print(marina.idade)
    print(marcos.idade)

    for filho in marcos.filhos:
        print(filho.nome)

    marcos.sobrenome = 'Ranes'
    print(marcos.sobrenome)
    print(marcos.__dict__)

    print(Pessoa.olhos)
    del marcos.filhos
    marcos.olhos = 1
    print(marcos.__dict__)
    print(marina.__dict__)
    print(marina.olhos)


