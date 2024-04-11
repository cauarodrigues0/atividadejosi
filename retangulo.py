class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):

        return 2 * (self.base + self.altura)
    
if __name__ == "__main__":
    r = retangulo(5, 20)

    print(r.area())

    print(r.perimetro())
