from Lab1.pessoa import Pessoas
class Funcionario(Pessoas):
    
    def __init__(nome,numero):
        Pessoas.__init__(nome,numero) #super().__init__(nome,numero) 