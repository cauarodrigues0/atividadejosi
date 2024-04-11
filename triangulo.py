class Triangulo:
    def __init__(self, a, b, c, altura, base):
        self.a = a
        self.b = b
        self.c = c
        self.altura = altura
        self.base = base

    def CalcularArea(self):
        area = (self.base * self.altura) / 2
        return area
    
    def CalcularPerimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro
    
if __name__ == "__main__":
    triangulo1 = Triangulo(3,4,5,6,4)
    triangulo2 = Triangulo(1,2,3,4,3)

    print(triangulo1.CalcularArea())
    print(triangulo2.CalcularPerimetro())

    

    