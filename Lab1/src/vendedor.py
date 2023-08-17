from lab1.funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self,nome,numero):
        self.faturas = []
        Funcionario.__init__(self,nome,numero) 

    
    def obter_faturas(self):
        return self.faturas    