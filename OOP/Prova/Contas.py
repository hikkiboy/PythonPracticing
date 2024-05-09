class Conta():
  def __init__(self,numero,cpf,saldo,ativo):
    self.Numero = numero
    self.Cpf = cpf
    self.Saldo = saldo
    self.Ativo = ativo
  def Ativar(self):
    if self.Ativo == False:
      self.Ativo = True
    else:
      print("Ja ativou")
  def Debito(self,valor):
    if self.Ativo == True and self.Saldo - valor >= 0 and valor > 0:
      self.Saldo = self.Saldo - valor
    else:
      print("nao")
  def Credito(self,valor):
    if self.Ativo == True and valor > 0 :
      self.Saldo = self.Saldo + valor


class Poupanca(Conta):
  def __init__(self,diaAniversario, numero,cpf,saldo,ativo):
    super().__init__(numero,cpf,saldo,ativo)
    self.diaAniversario = diaAniversario
  def Correcao(self,data):
    if(self.diaAniversario == data):
      self.Saldo = (self.Saldo * 0.05) + self.Saldo
    else:
       print("a")

class Corrente(Conta):
  def __init__(self, numero,cpf,saldo,ativo, nTalao):
    super().__init__(numero,cpf,saldo,ativo)
    self.NTalao = nTalao
  def Talao(self):
    if self.NTalao > 0:
        self.Saldo = self.Saldo - 30
    else:
       print("vc nao tem")


class Especial(Conta):
  def __init__(self,limite, numero,cpf,saldo,ativo):
    super().__init__(numero,cpf,saldo,ativo)
    self.Limite = limite
  def Debito(self, limite):
    if self.Saldo < 0:
      self.Saldo -= limite
    elif self.Saldo + self.Limite - limite >= 0:
       self.Limite = self.Limite + self.Saldo - limite
       self.Saldo = 0
    else:
       print("ta pedindo demais")

class Empresa(Conta):
    def __init__(self, numero,cpf,saldo,ativo,limEmprestimo):
        super().__init__(numero,cpf,saldo,ativo)
        self.LimEmpresitmo = limEmprestimo
    def Emprestimo(self, emprestimo):
        if emprestimo <= self.LimEmpresitmo:
            self.Saldo = emprestimo + self.Saldo
            self.LimEmpresitmo = self.LimEmpresitmo - emprestimo
        else:
           print("nao da nao mano")

class Estudantil (Conta):
    def __init__(self, numero,cpf,saldo,ativo,limite):
        super().__init__(numero,cpf,saldo,ativo)
        self.Limiteimite = limite
    def Emprestimo(self, emprestimo):
        if emprestimo <= self.Limiteimite:
            self.Saldo = emprestimo + self.Saldo
            self.Limiteimite = self.Limiteimite - emprestimo
        else:
           print("nao")








