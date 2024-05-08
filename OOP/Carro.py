class CarroPequeno:
    def __init__(self,marca,cor,motor,velocidade = 0,ligado = False):
        self.Marca = marca
        self.Cor = cor
        self.Motor = motor
        self.Velocidade = velocidade
        self.Ligado = ligado
    
    def ligaCarro(self):
        self.Ligado = True
        print("AAAAAAAAAAAAAAAA PARA")


    def alecerar(self):
        if self.Ligado :
            self.Velocidade += 1
            print(f"Velocidade = {self.Velocidade} VRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUM")
        


class Moto:
    def __init__(self, marca,cilindrada,velocidade=0, ligado = False) -> None:
        self.__marca = marca
        self.__cilindrada = cilindrada




class CarroGrande:
    def __init__(self,marca,cor,motor,velocidade = 0,ligado = False, grande = True):
        self.Marca = marca
        self.Cor = cor
        self.Motor = motor
        self.Velocidade = velocidade
        self.Ligado = ligado
        self.Grande = grande
