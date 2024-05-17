class Produti:
    def __init__(self,id,codigo,nome,valor,estoque) -> None:
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.estoque = estoque
    def incluirEstoque(self, valor):
        self.estoque = self.estoque + valor
    def removerEstoque ( self, valor):
        if valor <= 0:
            print('Impossivel man')
        elif valor > self.estoque:
            print("nao")
        else:
            self.estoque = self.estoque - valor 
    def __str__(self) -> str:
        return f'ID: {self.id} - nome: {self.nome} - cod:  {self.codigo}'