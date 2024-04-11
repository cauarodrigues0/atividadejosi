class Carro:
    def __init__(self, marca, modelo , ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"o {self.modelo} está ligado"
    
    def desligar(self):
        return f"o {self.modelo} está desligado"
    
    def acelerar(self):
        return f"o {self.modelo} está acelerando"

if __name__ == "__main__":
    carro1 = Carro("fiat", "touro", "1900","vermelha")
    carro2 = Carro("ford", "ka", "2020","branco")

    print(carro1.ligar())
    print(carro2.desligar())
    print(carro1.acelerar())


