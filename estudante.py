class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def media(self):
        media1 = self.nota / 4
        return media1
    
    def aprovado(self):
        mediaaluno = self.media()
        if mediaaluno >= 7:
            print(f"O estudante {self.nome} foi Aprovado")
        else:
            print(f"O estudante {self.nome} foi Reprovado")
    
if __name__ == "__main__":
    estudante1 = Estudante("João", 15, 40)
    estudante2 = Estudante("John", 16, 32)

    estudante1.aprovado()
    estudante2.aprovado()
