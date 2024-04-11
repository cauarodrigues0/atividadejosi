class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def som(self,som):
        return f'{self.nome} faz {som}'
    
    def info(self):
        return f"o {self.nome} tem: {self.idade} anos de idade e é da espécie {self.especie}"
        

if __name__ == '__main__':
    cachorro = Animal('Dog', 10, 'Cachorro')
    gato = Animal('Cat', 5, 'Gato')


    print(cachorro.som('auau'))
    print(gato.info())
