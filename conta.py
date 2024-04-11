class ContaBancaria:
    def __init__(self,n_conta, saldo, titular):
        self.n_conta = n_conta
        self.saldo = saldo
        self.titular = titular
    
    def deposito(self, valor):
        self.saldo += valor
        return self.saldo
    
    def saque(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def saldoatual(self):
        return self.saldo
    
if __name__ == '__main__':
    conta1 = ContaBancaria(1234, 1000, 'João')
    conta2 = ContaBancaria(4321, 1500, "Kethilly")

    print(conta1.deposito(100))
    print(conta1.saque(50))
    print(conta1.saldoatual())
    print(conta2.deposito(500))
    print(conta2.saldoatual)
    