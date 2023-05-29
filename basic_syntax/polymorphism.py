class Father:

    def __init__(self, numero):
        self.numero = numero

    def article(self):
        print('Articulo')

    def title(self):
        print('Titulo')

    def author(self):
        print('Autor')

class Children(Father):

    def __init__(self, numero):
        super().__init__(numero)

    def url(self):
        print('Url')

    def footer(self):
        print('Pie de pagina')

    def plus(self):
        print(self.numero + self.numero)

post = Children(4)
post.article()
post.url()
post.plus()