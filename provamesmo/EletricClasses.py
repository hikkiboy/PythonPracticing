class Usuario():
    def __init__(self, id, email, senha) -> None:
        self.id = id,
        self.email = email,
        self.senha = senha,

class ProdutoEletronico():
    def __init__(self,id_produtoeletronico,descricao,marca,valor,estoque) -> None:
        self.id_produtoeletronico = id_produtoeletronico,
        self.descricao = descricao,
        self.marca = marca,
        self.valor = valor,
        self.estoque = estoque
    def Incluir(self, valor):
        if valor > 0 and valor <= 10 and self.estoque < 10 and (self.estoque + valor) < 10:
            self.estoque = self.estoque + valor
        else:
            print("Valor invalido inserido, ou estoque cheio (capacidade maxima 10)")
    def Retirar(self,valor):
        if valor > 0 and (self.estoque - valor) >= 0:
            self.estoque = self.estoque - valor
        else:
            print("Valor invalido inserido")
        