class Produto:
    def __init__(self, nome, preço, quantidade_estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade_estoque = quantidade_estoque
    
    def atualizar(self, valor):
        self.quantidade_estoque += valor
        return self.quantidade_estoque
    
    def diminuir(self, valor):
        self.quantidade_estoque -= valor
        return self.quantidade_estoque

    def calcular_preço(self,quantidade):
        return self.preço * quantidade
    
if __name__ == "__main__":
    produto1 = Produto("Camiseta", 50, 20)
    produto2 = Produto("Calça", 100, 10)


    print(produto1.atualizar(10))
    print(produto2.diminuir(10))
    print(produto1.calcular_preço(3))
   