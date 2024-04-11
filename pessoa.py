class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Altura: {self.altura}')

    def cumprimentar(self):
        print(f'Olá, meu nome é {self.nome}')
        print(f'Tenho {self.idade} anos')
        print(f'Minha altura é {self.altura}')

if __name__ == "__main__":
    pessoa1 = Pessoa('Cauã', 20, 1.75)
    pessoa2 = Pessoa('Ket', 25, 1.65)

    print()
    pessoa1.info()
    pessoa1.cumprimentar()
    
    print()
    pessoa2.info()
    pessoa2.cumprimentar()