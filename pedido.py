class Pedido:
    def __init__(self, itens, total, status):
        self.itens = itens
        self.precos = total 
        self.status = status
        
    def add_item(self, item, preco):
        self.itens.append(item)
        self.precos.append(preco)
    
    def calculate_total(self): 
        total = sum(self.precos)
        return total

    def get_status(self):  
        return self.status
    
if __name__ == '__main__':
    pedido1 = Pedido(["Calça", "Camisa"], [100, 50], "entregue")
    pedido2 = Pedido(["Legging", "Top"], [100, 30], "a caminho")

    pedido1.add_item("Short", 40)  
    print(pedido1.calculate_total()) 
    print(pedido2.calculate_total())
    print(pedido1.get_status())
    print(pedido2.get_status())  
