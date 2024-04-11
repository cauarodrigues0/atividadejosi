class Pedido:
    def __init__(self,itens,total,status):
        self.itens = itens
        self.total = total
        self.status = status
        
    def item(self,item):
        self.itens.append(item)
    
    def total(self):
        self.item = 0
        for item in self.itens:
            self.item += item
        return self.item

    def status(self,status):
        print(f'entregue')
    
if __name__ == '__main__':
    pedido1 = Pedido('Camiseta',100)
    pedido2 = Pedido('Calça',200)

    print(f'Total: {pedido2.total}')
    print(f'Status: {pedido2.status}')
    pedido2.status('Entregue')
    print(f'Status: {pedido2.status}')

    print(f'Total: {pedido1.total}')
    print(f'Status: {pedido1.status}')
    pedido1.status('Entregue')
    print(f'Status: {pedido1.status}')

    