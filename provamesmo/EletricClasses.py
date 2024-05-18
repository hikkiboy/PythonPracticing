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
    def Incluir(self, qntd):
        if qntd > 0 and qntd < 10 and self.estoque < 10:
            self.estoque = self.estoque + qntd
        else:
            print("não ta rolando legal amigo")
    def Retirar(self,valor):
        if valor > 0 and valor <= 10 and self.estoque < 10 and (self.estoque + valor) < 10:
            self.estoque = self.estoque - valor
        else:
            print("não ta rolando legal")
        