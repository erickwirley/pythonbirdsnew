class Pessoa:
    def __init__(self, name= None, idade= 0):
        self.idade = idade
        self.nome = name


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('teste')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Erick'
    print(p.nome)
    print(p.idade)
