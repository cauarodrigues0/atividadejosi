class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def info(self):
        print(f"o livro {self.titulo} do autor {self.autor} tem {self.paginas} paginas")
    
    def PalavrasPorPagina(self,palavras):
        palavrasppagina = palavras/self.paginas
        print(f"o livro {self.titulo} tem {palavrasppagina} palavras por página")
    
if __name__ == '__main__':
    livro1 = Livro("Python Rocks!","Geek University",500)
    livro2 = Livro("O Pior Dia de Todos","Ciclana",32)

    livro1.info()
    livro2.info()

    livro1.PalavrasPorPagina(15000)
    livro2.PalavrasPorPagina(1200)